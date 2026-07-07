# -*- coding: utf-8 -*-
"""
モンハンサンブレイク 傀異化素材検索 Discord bot

ユーザーが素材名（漢字 or ひらがな）を打つと、部分一致でカテゴリを検索。
候補が複数ならボタンで選ばせ、確定したカテゴリの素材名+モンスター名を返す。
結果メッセージの 📩 リアクションを押すと、URLをDMで受け取れる。
"""

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from data import MATERIALS, MONSTERS

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def parse_allowed_channel_ids(raw: str | None) -> set[int]:
    """カンマ区切りのチャンネルID文字列をパースする。未設定・空なら空集合(=全チャンネル許可)。"""
    if not raw:
        return set()
    ids = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if not part.isdigit():
            raise SystemExit(
                f"ALLOWED_CHANNEL_IDS の値が不正です: {part!r} (数字のチャンネルIDをカンマ区切りで指定してください)"
            )
        ids.add(int(part))
    return ids


# 反応するチャンネルのID集合。空なら全チャンネルで反応する。
ALLOWED_CHANNEL_IDS = parse_allowed_channel_ids(os.getenv("ALLOWED_CHANNEL_IDS"))

# 結果メッセージのID → モンスター名リスト の対応を保持する辞書。
# 📩 リアクションが押されたとき、どのメッセージがどのモンスター群に対応するか引くために使う。
# メモリ上で持つだけなので bot 再起動で消える（永続化は不要）。
result_message_registry: dict[int, list[str]] = {}


# ─── ロジック層（Discord に依存しない） ─────────────────

def search_categories(query: str) -> dict[str, dict]:
    """入力文字で MATERIALS を部分一致検索し、ヒットしたカテゴリ名→データの辞書を返す。

    照合対象: カテゴリ名(漢字キー) + alias(あれば) + yomi(あれば)
    そのいずれかに query が部分一致(in)すればヒット。
    """
    hits = {}
    for category_name, info in MATERIALS.items():
        # 照合対象を1つのリストにまとめる
        targets = [category_name]
        targets += info.get("alias", [])
        targets += info.get("yomi", [])

        # いずれかの照合対象に入力が含まれていればヒット
        if any(query in t for t in targets):
            hits[category_name] = info
    return hits


def build_result_text(category_name: str, info: dict) -> str:
    """カテゴリ確定後のチャンネル向け返信テキストを組み立てる。

    フォーマット:
      素材名3段階（tiers）を改行で
      （空行）
      モンスター名を改行で
    """
    lines = list(info["tiers"])
    lines.append("")  # 空行
    lines += info["monsters"]
    return "\n".join(lines)


def build_dm_text(monster_names: list[str]) -> str:
    """DM用のURL一覧テキストを組み立てる。"""
    lines = []
    for name in monster_names:
        url = MONSTERS[name]
        lines.append(f"{name} {url}")
    return "\n".join(lines)


# ─── ボタン UI ──────────────────────────────────────

# discord.ui.View はボタンやセレクトメニューなど「メッセージに付く部品」の入れ物。
# View を継承して、中にボタンを追加していく。
class CategorySelectView(discord.ui.View):
    """候補カテゴリの選択ボタンを並べる View。"""

    def __init__(self, hits: dict[str, dict]):
        # timeout=60 → 60秒操作がないとボタンが無効になる
        super().__init__(timeout=60)

        # ヒットしたカテゴリごとにボタンを動的に追加する。
        # カテゴリ数が素材によって変わるので、ループで追加するのが汎用的。
        for category_name, info in hits.items():
            button = CategoryButton(category_name, info)
            self.add_item(button)

    async def on_timeout(self):
        """タイムアウトしたらボタンを全部無効化して見た目を更新する。"""
        for item in self.children:
            item.disabled = True
        if hasattr(self, "message"):
            await self.message.edit(view=self)


# discord.ui.Button を継承して、押された時の処理 (callback) を定義する。
class CategoryButton(discord.ui.Button):
    """カテゴリ1つ分のボタン。"""

    def __init__(self, category_name: str, info: dict):
        # label: ボタンに表示する文字
        # style: ボタンの色（primary=青, secondary=灰, success=緑, danger=赤）
        super().__init__(label=category_name, style=discord.ButtonStyle.primary)
        self.category_name = category_name
        self.info = info

    async def callback(self, interaction: discord.Interaction):
        """ボタンが押されたときに Discord が呼び出すメソッド。

        interaction は「誰がどのボタンを押したか」などの情報を持つオブジェクト。
        interaction.response.edit_message() で元のメッセージを結果に書き換える。
        """
        text = build_result_text(self.category_name, self.info)

        # ボタンを全部無効化して「選択済み」にする
        for item in self.view.children:
            item.disabled = True

        await interaction.response.edit_message(content=text, view=self.view)

        # 編集後のメッセージを取得して 📩 リアクションを付ける
        # interaction.message は編集前の参照なので、fetch して最新を取得
        msg = await interaction.original_response()
        await msg.add_reaction("📩")

        # メッセージID → モンスターリスト を登録（📩 押下時にURLを引くため）
        result_message_registry[msg.id] = self.info["monsters"]


# ─── Bot 本体 ───────────────────────────────────────

# intents は「botがどの情報を受け取るか」の設定。
# message_content: メッセージの中身を読むために必要。
# reactions: リアクションの追加を検知するために必要。
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")


@bot.event
async def on_message(message: discord.Message):
    # bot 自身の発言には反応しない（無限ループ防止）
    if message.author == bot.user:
        return

    # チャンネル制限が設定されていれば、対象外のチャンネルには反応しない
    if ALLOWED_CHANNEL_IDS and message.channel.id not in ALLOWED_CHANNEL_IDS:
        return

    query = message.content.strip()
    if not query:
        return

    hits = search_categories(query)

    # ヒット0件 → 素材名に該当しない通常の発言なので黙る
    if not hits:
        return

    # ヒット1件 → ボタンなしで即座に結果を返す
    if len(hits) == 1:
        category_name, info = next(iter(hits.items()))
        text = build_result_text(category_name, info)
        sent = await message.channel.send(text)

        # 📩 リアクションを付けて、メッセージID→モンスターリストを登録
        await sent.add_reaction("📩")
        result_message_registry[sent.id] = info["monsters"]
        return

    # ヒット複数 → ボタンで選ばせる
    view = CategorySelectView(hits)
    sent = await message.channel.send(
        f"「{query}」の検索結果が複数あります。どれを調べますか？",
        view=view,
    )
    # タイムアウト時にメッセージを編集できるよう参照を保存
    view.message = sent


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    """リアクションが追加されたときに呼ばれるイベント。

    on_reaction_add ではなく on_raw_reaction_add を使う理由:
    on_reaction_add はメッセージがキャッシュにある場合しか発火しない。
    bot再起動直後やキャッシュが飛んだ場合に取りこぼすので、
    常に発火する raw 版を使うのが安全。
    """
    # bot 自身がつけたリアクション（初期の📩）には反応しない
    if payload.user_id == bot.user.id:
        return

    # 📩 以外のリアクションは無視
    if str(payload.emoji) != "📩":
        return

    # このメッセージが結果メッセージとして登録されているか確認
    monster_names = result_message_registry.get(payload.message_id)
    if monster_names is None:
        return

    # DM用テキストを組み立てて送信
    dm_text = build_dm_text(monster_names)

    # payload.member はギルド内でのみ取得できる。DMの場合は None なので、
    # bot.fetch_user で確実にユーザーを取得する。
    user = payload.member or await bot.fetch_user(payload.user_id)

    try:
        await user.send(dm_text)
    except discord.Forbidden:
        # ユーザーがDMを拒否している場合、チャンネルに通知する
        channel = bot.get_channel(payload.channel_id)
        if channel:
            await channel.send(f"{user.mention} DMを送れませんでした（DM設定をご確認ください）")


bot.run(TOKEN)

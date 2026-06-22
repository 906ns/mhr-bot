# -*- coding: utf-8 -*-
"""
モンハンサンブレイク 傀異化素材検索 Discord bot

ユーザーが素材名を打つと、入手元モンスターとURLを返す。
系統が複数ある素材はボタンで選ばせる。
"""

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from data import MATERIALS, MONSTERS

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ─── ロジック層（Discord に依存しない） ─────────────────

def search_material(name: str) -> dict[str, list[str]] | None:
    """素材名から系統→モンスター名リストの辞書を返す。見つからなければ None。"""
    return MATERIALS.get(name)


def build_result_text(material_name: str, variant: str, monster_names: list[str]) -> str:
    """系統が確定した後の返信テキストを組み立てる。"""
    header = f"【{material_name}（{variant}）】"
    lines = [header]
    for m in monster_names:
        url = MONSTERS[m]
        lines.append(f"　{m}　{url}")
    return "\n".join(lines)


# ─── ボタン UI ──────────────────────────────────────

# discord.ui.View はボタンやセレクトメニューなど「メッセージに付く部品」の入れ物。
# View を継承して、中にボタンを追加していく。
class VariantSelectView(discord.ui.View):
    """系統選択ボタンを並べる View。"""

    def __init__(self, material_name: str, variants: dict[str, list[str]]):
        # timeout=60 → 60秒操作がないとボタンが無効になる
        super().__init__(timeout=60)
        self.material_name = material_name

        # 系統ごとにボタンを動的に追加する。
        # discord.ui.Button はデコレータでも作れるが、
        # 系統の数が素材によって変わるので、ループで動的に追加するほうが汎用的。
        for variant, monsters in variants.items():
            button = VariantButton(material_name, variant, monsters)
            self.add_item(button)

    async def on_timeout(self):
        """タイムアウトしたらボタンを全部無効化して見た目を更新する。"""
        for item in self.children:
            item.disabled = True
        # self.message は send 時に返ってくるメッセージを後から代入して使う
        if hasattr(self, "message"):
            await self.message.edit(view=self)


# discord.ui.Button を継承して、押された時の処理 (callback) を定義する。
class VariantButton(discord.ui.Button):
    """系統1つ分のボタン。"""

    def __init__(self, material_name: str, variant: str, monsters: list[str]):
        # label: ボタンに表示する文字
        # style: ボタンの色（primary=青, secondary=灰, success=緑, danger=赤）
        super().__init__(label=variant, style=discord.ButtonStyle.primary)
        self.material_name = material_name
        self.variant = variant
        self.monsters = monsters

    async def callback(self, interaction: discord.Interaction):
        """ボタンが押されたときに Discord が呼び出すメソッド。

        interaction は「誰がどのボタンを押したか」などの情報を持つオブジェクト。
        interaction.response.send_message() で押した人にだけ見える返信もできるが、
        ここではチャンネル全体に見えるように edit_message() で元メッセージを書き換える。
        """
        text = build_result_text(self.material_name, self.variant, self.monsters)

        # ボタンを全部無効化して「選択済み」にする
        for item in self.view.children:
            item.disabled = True

        await interaction.response.edit_message(content=text, view=self.view)


# ─── Bot 本体 ───────────────────────────────────────

# intents は「botがどの情報を受け取るか」の設定。
# message_content を有効にしないとメッセージの中身が読めない。
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")


@bot.event
async def on_message(message: discord.Message):
    # bot 自身の発言には反応しない（無限ループ防止）
    if message.author == bot.user:
        return

    material_name = message.content.strip()
    variants = search_material(material_name)

    # 該当する素材がなければ何もしない（通常の会話に反応しない）
    if variants is None:
        return

    # 系統が1つだけ → ボタンなしで即回答
    if len(variants) == 1:
        variant, monsters = next(iter(variants.items()))
        text = build_result_text(material_name, variant, monsters)
        await message.channel.send(text)
        return

    # 系統が複数 → ボタンで選ばせる
    view = VariantSelectView(material_name, variants)
    sent = await message.channel.send(
        f"「{material_name}」のどの系統を調べますか？",
        view=view,
    )
    # タイムアウト時にメッセージを編集できるよう参照を保存
    view.message = sent


bot.run(TOKEN)

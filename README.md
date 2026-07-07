# モンハンサンブレイク 傀異化素材検索 Discord Bot

素材名（漢字・ひらがな）を打つと、傀異化素材の正式名とモンスターを返す Discord bot です。
📩 リアクションを押すと攻略ページのURLをDMで受け取れます。

## セットアップ

### 1. Discord Bot トークンを取得

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. 「New Application」でアプリを作成
3. 左メニュー「Bot」→「Add Bot」
4. 「TOKEN」欄の「Reset Token」でトークンを取得（一度しか表示されないのでコピー）
5. 同じ画面の **Privileged Gateway Intents** で **MESSAGE CONTENT INTENT** を **ON** にする

### 2. Bot をサーバーに招待

1. 左メニュー「OAuth2」→「URL Generator」
2. SCOPES で `bot` にチェック
3. BOT PERMISSIONS で `Send Messages`、`Add Reactions` にチェック
4. 生成された URL をブラウザで開き、サーバーを選んで招待

### 3. 環境構築と起動

```bash
# リポジトリをクローン
git clone https://github.com/906ns/mhr-bot.git
cd mhr-bot

# 仮想環境を作成して有効化
python -m venv .venv
.venv\Scripts\activate

# パッケージをインストール
pip install -r requirements.txt

# .env.example をコピーして .env を作成し、トークンを設定（メモ帳などで編集してOK）
copy .env.example .env

# 起動
python bot.py
```

「ログイン完了: BotName#1234」と表示されれば成功です。

### 4. 反応するチャンネルを制限する（任意）

`.env` の `ALLOWED_CHANNEL_IDS` に、反応させたいチャンネルのIDをカンマ区切りで設定します。

```
ALLOWED_CHANNEL_IDS=123456789012345678,234567890123456789
```

- 空 or 未設定の場合は、すべてのチャンネルで反応します
- チャンネルIDは、Discord の設定で「開発者モード」を ON にし、チャンネルを右クリック →「チャンネルIDをコピー」で取得できます

## 使い方

チャンネルに素材名（漢字 or ひらがな）を打つだけです。

- 漢字入力: `骨` → 骨/凶骨/竜骨/龍骨 など部分一致でヒット
- ひらがな入力: `つめ` → 爪/凶爪 がヒット
- 候補が1件 → そのまま結果を返します
- 候補が複数 → ボタンで選ぶと結果を返します
- 結果メッセージの 📩 を押すと、モンスターの攻略URLがDMで届きます
- 素材名に一致しない発言には反応しません

## ファイル構成

| ファイル | 役割 |
|---|---|
| `bot.py` | Discord bot 本体（検索・ボタン UI・リアクション・DM送信） |
| `data.py` | 素材・モンスターのデータ定義 |
| `.env` | Discord トークン・チャンネル設定（Git管理外） |
| `.env.example` | `.env` のテンプレート |
| `.gitignore` | `.env` 等を除外 |
| `requirements.txt` | 依存パッケージ |

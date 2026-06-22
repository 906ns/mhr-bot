# モンハンサンブレイク 傀異化素材検索 Discord Bot

素材名を打つと、その傀異化素材を入手できるモンスター名と攻略ページURLを返す Discord bot です。

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
3. BOT PERMISSIONS で `Send Messages` にチェック
4. 生成された URL をブラウザで開き、サーバーを選んで招待

### 3. 環境構築と起動

```bash
# リポジトリをクローン
git clone <リポジトリURL>
cd mhr-bot

# 仮想環境を作成して有効化
python -m venv .venv
.venv\Scripts\activate

# パッケージをインストール
pip install -r requirements.txt

# .env ファイルを作成してトークンを設定（メモ帳などで作ってもOK）
echo DISCORD_TOKEN=ここにトークンを貼る > .env

# 起動
python bot.py
```

「ログイン完了: BotName#1234」と表示されれば成功です。

## 使い方

チャンネルに素材名（例: `爪`、`骨`、`鱗`）を打つだけです。

- 系統が1つの素材 → そのまま結果を返します
- 系統が複数ある素材 → ボタンで系統を選ぶと結果を返します
- 素材名に一致しない発言には反応しません

## ファイル構成

| ファイル | 役割 |
|---|---|
| `bot.py` | Discord bot 本体（イベント処理・ボタン UI） |
| `data.py` | 素材・モンスターのデータ定義 |
| `.env` | Discord トークン（Git管理外） |
| `.gitignore` | `.env` 等を除外 |
| `requirements.txt` | 依存パッケージ |

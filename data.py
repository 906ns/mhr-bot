# -*- coding: utf-8 -*-
"""
モンハンサンブレイク 傀異化素材データ

データ出典:
  入手元モンスター・素材名 … AppMedia 傀異化素材一覧 https://appmedia.jp/mhrise/75715234
  モンスターURL            … モンハンライズ攻略レシピ https://mhrise.com/data/4211.html

構造:
  MONSTERS  … モンスター名 → URL（URLはここ1箇所で管理し重複させない）
  MATERIALS … 素材カテゴリ名 → {"alias": [漢字の別名(任意)], "yomi": [ひらがな読み], "tiers": [レア度3段階の素材名], "monsters": [入手元モンスター名]}

検索の考え方:
  ユーザーが入力した文字を「素材カテゴリ名の一部に含む」キーをすべて拾う(部分一致)。
  漢字でもひらがな(yomi)でも照合する。例:「骨」「ほね」どちらでも 骨/凶骨/竜骨/龍骨 がヒット。
     1つだけヒットなら選択を出さず即結果。
"""

# ───────────────────────────────────────────
# モンスター名 → URL
# ───────────────────────────────────────────
MONSTERS = {
    "アオアシラ": "https://mhrise.com/data/4446.html",
    "ラングロトラ": "https://mhrise.com/data/4490.html",
    "ウルクスス": "https://mhrise.com/data/4456.html",
    "オサイズチ": "https://mhrise.com/data/4443.html",
    "ドスバギィ": "https://mhrise.com/data/4458.html",
    "クルルヤック": "https://mhrise.com/data/4462.html",
    "ドスフロギィ": "https://mhrise.com/data/4451.html",
    "ロアルドロス": "https://mhrise.com/data/4450.html",
    "ボルボロス": "https://mhrise.com/data/4501.html",
    "アケノシルム": "https://mhrise.com/data/4442.html",
    "バサルモス": "https://mhrise.com/data/4466.html",
    "ダイミョウザザミ": "https://mhrise.com/data/4544.html",
    "フルフル": "https://mhrise.com/data/4453.html",
    "ヨツミワドウ": "https://mhrise.com/data/4444.html",
    "ビシュテンゴ": "https://mhrise.com/data/4449.html",
    "リオレイア": "https://mhrise.com/data/4460.html",
    "トビカガチ": "https://mhrise.com/data/4447.html",
    "プケプケ": "https://mhrise.com/data/4464.html",
    "アンジャナフ": "https://mhrise.com/data/4461.html",
    "ビシュテンゴ亜種": "https://mhrise.com/data/4533.html",
    "イソネミクニ": "https://mhrise.com/data/4448.html",
    "ショウグンギザミ": "https://mhrise.com/data/4534.html",
    "ジュラトドス": "https://mhrise.com/data/4463.html",
    "ナルガクルガ": "https://mhrise.com/data/4508.html",
    "マガイマガド": "https://mhrise.com/data/4441.html",
    "ガランゴルム": "https://mhrise.com/data/4530.html",
    "ベリオロス": "https://mhrise.com/data/4457.html",
    "ゴシャハギ": "https://mhrise.com/data/4455.html",
    "オロミドロ": "https://mhrise.com/data/4491.html",
    "ヤツカダキ": "https://mhrise.com/data/4465.html",
    "イソネミクニ亜種": "https://mhrise.com/data/4538.html",
    "ルナガロン": "https://mhrise.com/data/4531.html",
    "オロミドロ亜種": "https://mhrise.com/data/4539.html",
    "ティガレックス": "https://mhrise.com/data/4454.html",
    "リオレウス": "https://mhrise.com/data/4459.html",
    "ライゼクス": "https://mhrise.com/data/4532.html",
    "タマミツネ": "https://mhrise.com/data/4452.html",
    "ディアブロス": "https://mhrise.com/data/4492.html",
    "ジンオウガ": "https://mhrise.com/data/4483.html",
    "セルレギオス": "https://mhrise.com/data/4537.html",
    "ゴア・マガラ": "https://mhrise.com/data/4542.html",
    "エスピナス": "https://mhrise.com/data/4543.html",
    "バゼルギウス": "https://mhrise.com/data/4523.html",
    "ラージャン": "https://mhrise.com/data/4493.html",
    "ヤツカダキ亜種": "https://mhrise.com/data/4545.html",
    "リオレウス希少種": "https://mhrise.com/data/4588.html",
    "リオレイア希少種": "https://mhrise.com/data/4587.html",
    "エスピナス亜種": "https://mhrise.com/data/4590.html",
    "紅蓮滾るバゼルギウス": "https://mhrise.com/data/4575.html",
    "激昂したラージャン": "https://mhrise.com/data/4574.html",
    "怨嗟響めくマガイマガド": "https://mhrise.com/data/4573.html",
    "傀異克服オオナズチ": "https://mhrise.com/data/4592.html",
    "傀異克服クシャルダオラ": "https://mhrise.com/data/4595.html",
    "傀異克服テオ・テスカトル": "https://mhrise.com/data/4594.html",
    "傀異克服バルファルク": "https://mhrise.com/data/4598.html",
    "傀異克服シャガルマガラ": "https://mhrise.com/data/4600.html",
}

# ───────────────────────────────────────────
# 素材カテゴリ名 → レア度3段階の素材名 + 入手元モンスター
# ───────────────────────────────────────────
MATERIALS = {
    # 通常系
    "骨": {
        "yomi": ["ほね"],
        "tiers": ["傀異化した骨", "傀異化した堅骨", "傀異化した重骨"],
        "monsters": ["アオアシラ", "ラングロトラ", "ウルクスス"],
    },
    "皮": {
        "yomi": ["かわ"],
        "tiers": ["傀異化した皮", "傀異化した上皮", "傀異化した厚皮"],
        "monsters": ["オサイズチ", "ドスバギィ", "クルルヤック", "ドスフロギィ"],
    },
    "竜骨": {
        "yomi": ["りゅうこつ"],
        "tiers": ["傀異化した竜骨", "傀異化した堅竜骨", "傀異化した重竜骨"],
        "monsters": ["ロアルドロス", "ボルボロス", "アケノシルム", "バサルモス"],
    },
    "血": {
        "yomi": ["ち"],
        "tiers": ["傀異化した血", "傀異化した浄血", "傀異化した浄濃血"],
        "monsters": ["ダイミョウザザミ", "フルフル", "ヨツミワドウ", "ビシュテンゴ"],
    },
    "鱗": {
        "yomi": ["うろこ"],
        "tiers": ["傀異化した鱗", "傀異化した上鱗", "傀異化した厚鱗"],
        "monsters": ["リオレイア", "トビカガチ", "プケプケ", "アンジャナフ"],
    },
    "殻": {
        "alias": ["甲殻"],
        "yomi": ["から", "こうかく"],
        "tiers": ["傀異化した甲殻", "傀異化した堅殻", "傀異化した重殻"],
        "monsters": ["ビシュテンゴ亜種", "イソネミクニ", "ショウグンギザミ", "ジュラトドス"],
    },
    "牙": {
        "yomi": ["きば"],
        "tiers": ["傀異化した牙", "傀異化した鋭牙", "傀異化した重牙"],
        "monsters": ["ナルガクルガ", "マガイマガド", "ガランゴルム", "ベリオロス"],
    },
    "爪": {
        "yomi": ["つめ"],
        "tiers": ["傀異化した爪", "傀異化した尖爪", "傀異化した剛爪"],
        "monsters": ["ゴシャハギ", "オロミドロ", "ヤツカダキ", "イソネミクニ亜種"],
    },
    # 凶系
    "凶骨": {
        "yomi": ["ほね", "きょうこつ", "きょうほね"],
        "tiers": ["傀異化した凶骨", "傀異化した凶堅骨", "傀異化した凶重骨"],
        "monsters": ["ルナガロン", "オロミドロ亜種", "ティガレックス"],
    },
    "凶鱗": {
        "yomi": ["うろこ", "きょううろこ", "きょうりん"],
        "tiers": ["傀異化した凶鱗", "傀異化した凶上鱗", "傀異化した凶厚鱗"],
        "monsters": ["リオレウス", "ライゼクス", "タマミツネ"],
    },
    "凶角": {
        "yomi": ["つの", "きょうつの", "きょうかく"],
        "tiers": ["傀異化した凶角", "傀異化した凶尖角", "傀異化した凶剛角"],
        "monsters": ["ディアブロス", "ジンオウガ", "セルレギオス"],
    },
    "凶殻": {
        "yomi": ["から", "こうかく", "きょうから", "きょうかく"],
        "tiers": ["傀異化した凶殻", "傀異化した凶堅殻", "傀異化した凶重殻"],
        "monsters": ["ゴア・マガラ", "エスピナス", "バゼルギウス"],
    },
    "凶爪": {
        "yomi": ["つめ", "きょうづめ", "きょうそう"],
        "tiers": ["傀異化した凶爪", "傀異化した凶尖爪", "傀異化した凶剛爪"],
        "monsters": ["ラージャン", "ヤツカダキ亜種"],
    },
    "凶翼膜": {
        "yomi": ["よくまく", "つばさ", "きょうよくまく"],
        "tiers": ["傀異化した凶翼膜", "傀異化した凶翼", "傀異化した凶剛翼"],
        "monsters": ["リオレウス希少種", "リオレイア希少種"],
    },
    "凶血": {
        "yomi": ["ち", "きょうけつ", "きょうち"],
        "tiers": ["傀異化した凶血", "傀異化した凶浄血", "傀異化した凶濃血"],
        "monsters": ["エスピナス亜種", "紅蓮滾るバゼルギウス"],
    },
    "凶牙": {
        "yomi": ["きば", "きょうきば", "きょうが"],
        "tiers": ["傀異化した凶牙", "傀異化した凶鋭牙", "傀異化した凶重牙"],
        "monsters": ["激昂したラージャン", "怨嗟響めくマガイマガド"],
    },
    # 破傀系（傀異克服モンスター由来）
    "龍骨": {
        "yomi": ["りゅうこつ", "りゅうほね"],
        "tiers": ["傀異化した龍骨", "傀異化した堅龍骨", "傀異化した重龍骨"],
        "monsters": ["傀異克服オオナズチ", "傀異克服クシャルダオラ", "傀異克服テオ・テスカトル"],
    },
    "龍血": {
        "yomi": ["りゅうけつ", "りゅうち"],
        "tiers": ["傀異化した龍血", "傀異化した浄龍血", "傀異化した濃龍血"],
        "monsters": ["傀異克服バルファルク", "傀異克服シャガルマガラ"],
    },
}

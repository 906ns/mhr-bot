# -*- coding: utf-8 -*-
"""
モンハンサンブレイク 傀異化素材データ

データ出典: AppMedia 傀異化素材一覧
https://appmedia.jp/mhrise/75715234

構造:
  MONSTERS  … モンスター名 → URL（URLはここ1箇所で管理し重複させない）
  MATERIALS … 素材の種類 → 系統(通常系/凶系) → そのモンスター名リスト

補足:
  - 素材のレア度違い(例: 爪/尖爪/剛爪)は入手元モンスターが同じなので区別しない。
  - 「通常系」と「凶系」は入手元モンスターが異なるので系統として分けている。
  - 通常系が存在しない素材(例: 翼膜)は「凶系」のみを持つ。
"""

# ───────────────────────────────────────────
# モンスター名 → URL
# ───────────────────────────────────────────
MONSTERS = {
    # 骨系
    "アオアシラ": "https://appmedia.jp/mhrise/6123526",
    "ラングロトラ": "https://appmedia.jp/mhrise/6123538",
    "ウルクスス": "https://appmedia.jp/mhrise/6123550",
    # 皮系
    "オサイズチ": "https://appmedia.jp/mhrise/6123520",
    "ドスバギィ": "https://appmedia.jp/mhrise/6123556",
    "クルルヤック": "https://appmedia.jp/mhrise/6130000",
    "ドスフロギィ": "https://appmedia.jp/mhrise/6123574",
    # 竜骨系
    "ロアルドロス": "https://appmedia.jp/mhrise/6123571",
    "ボルボロス": "https://appmedia.jp/mhrise/6129994",
    "アケノシルム": "https://appmedia.jp/mhrise/6123577",
    "バサルモス": "https://appmedia.jp/mhrise/6123535",
    # 血系
    "ダイミョウザザミ": "https://appmedia.jp/mhrise/75696292",
    "フルフル": "https://appmedia.jp/mhrise/6123553",
    "ヨツミワドウ": "https://appmedia.jp/mhrise/6123580",
    "ビシュテンゴ": "https://appmedia.jp/mhrise/6123568",
    # 鱗系
    "リオレイア": "https://appmedia.jp/mhrise/6123517",
    "トビカガチ": "https://appmedia.jp/mhrise/6130006",
    "プケプケ": "https://appmedia.jp/mhrise/6130009",
    "アンジャナフ": "https://appmedia.jp/mhrise/6129997",
    # 甲殻系
    "ビシュテンゴ亜種": "https://appmedia.jp/mhrise/75696493",
    "イソネミクニ": "https://appmedia.jp/mhrise/6123565",
    "ショウグンギザミ": "https://appmedia.jp/mhrise/75696748",
    "ジュラトドス": "https://appmedia.jp/mhrise/6130003",
    # 牙系
    "ナルガクルガ": "https://appmedia.jp/mhrise/6123586",
    "マガイマガド": "https://appmedia.jp/mhrise/6123529",
    "ガランゴルム": "https://appmedia.jp/mhrise/75696697",
    "ベリオロス": "https://appmedia.jp/mhrise/6123559",
    # 爪系
    "ゴシャハギ": "https://appmedia.jp/mhrise/6123547",
    "オロミドロ": "https://appmedia.jp/mhrise/6123541",
    "ヤツカダキ": "https://appmedia.jp/mhrise/6123532",
    "イソネミクニ亜種": "https://appmedia.jp/mhrise/75697477",
    # 凶骨系
    "ルナガロン": "https://appmedia.jp/mhrise/75737200",
    "オロミドロ亜種": "https://appmedia.jp/mhrise/75762640",
    "ティガレックス": "https://appmedia.jp/mhrise/6123562",
    # 凶鱗系
    "リオレウス": "https://appmedia.jp/mhrise/6129991",
    "ライゼクス": "https://appmedia.jp/mhrise/75617596",
    "タマミツネ": "https://appmedia.jp/mhrise/6123523",
    # 凶角系
    "ディアブロス": "https://appmedia.jp/mhrise/6123544",
    "ジンオウガ": "https://appmedia.jp/mhrise/6123583",
    "セルレギオス": "https://appmedia.jp/mhrise/75756916",
    # 凶殻系
    "ゴア・マガラ": "https://appmedia.jp/mhrise/75762775",
    "エスピナス": "https://appmedia.jp/mhrise/75737335",
    "バゼルギウス": "https://appmedia.jp/mhrise/6337576",
    # 凶爪系
    "ラージャン": "https://appmedia.jp/mhrise/6129847",
    "ヤツカダキ亜種": "https://appmedia.jp/mhrise/75777412",
    # 凶翼膜系
    "リオレウス希少種": "https://appmedia.jp/mhrise/75880516",
    "リオレイア希少種": "https://appmedia.jp/mhrise/75880906",
    # 凶血系
    "エスピナス亜種": "https://appmedia.jp/mhrise/76054655",
    "紅蓮滾るバゼルギウス": "https://appmedia.jp/mhrise/75876010",
    # 凶牙系
    "激昂したラージャン": "https://appmedia.jp/mhrise/75777466",
    "怨嗟響めくマガイマガド": "https://appmedia.jp/mhrise/75777499",
    # 破傀の龍骨・龍血系
    "傀異克服オオナズチ": "https://appmedia.jp/mhrise/76059647",
    "傀異克服クシャルダオラ": "https://appmedia.jp/mhrise/76234993",
    "傀異克服テオ・テスカトル": "https://appmedia.jp/mhrise/76235005",
    "傀異克服バルファルク": "https://appmedia.jp/mhrise/76449400",
    "傀異克服シャガルマガラ": "https://appmedia.jp/mhrise/76732172",
}

# ───────────────────────────────────────────
# 素材の種類 → 系統 → モンスター名リスト
# ───────────────────────────────────────────
MATERIALS = {
    "骨": {
        "通常系": ["アオアシラ", "ラングロトラ", "ウルクスス"],
        "凶系": ["ルナガロン", "オロミドロ亜種", "ティガレックス"],
    },
    "皮": {
        "通常系": ["オサイズチ", "ドスバギィ", "クルルヤック", "ドスフロギィ"],
    },
    "竜骨": {
        "通常系": ["ロアルドロス", "ボルボロス", "アケノシルム", "バサルモス"],
    },
    "血": {
        "通常系": ["ダイミョウザザミ", "フルフル", "ヨツミワドウ", "ビシュテンゴ"],
        "凶系": ["エスピナス亜種", "紅蓮滾るバゼルギウス"],
    },
    "鱗": {
        "通常系": ["リオレイア", "トビカガチ", "プケプケ", "アンジャナフ"],
        "凶系": ["リオレウス", "ライゼクス", "タマミツネ"],
    },
    "甲殻": {
        "通常系": ["ビシュテンゴ亜種", "イソネミクニ", "ショウグンギザミ", "ジュラトドス"],
        "凶系": ["ゴア・マガラ", "エスピナス", "バゼルギウス"],
    },
    "牙": {
        "通常系": ["ナルガクルガ", "マガイマガド", "ガランゴルム", "ベリオロス"],
        "凶系": ["激昂したラージャン", "怨嗟響めくマガイマガド"],
    },
    "爪": {
        "通常系": ["ゴシャハギ", "オロミドロ", "ヤツカダキ", "イソネミクニ亜種"],
        "凶系": ["ラージャン", "ヤツカダキ亜種"],
    },
    "角": {
        "凶系": ["ディアブロス", "ジンオウガ", "セルレギオス"],
    },
    "翼膜": {
        "凶系": ["リオレウス希少種", "リオレイア希少種"],
    },
    "龍骨": {
        "破傀": ["傀異克服オオナズチ", "傀異克服クシャルダオラ", "傀異克服テオ・テスカトル"],
    },
    "龍血": {
        "破傀": ["傀異克服バルファルク", "傀異克服シャガルマガラ"],
    },
}

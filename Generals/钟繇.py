# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:16,
# HeroInfoKey.武力成长:0.21,
# HeroInfoKey.初始智力:81,
# HeroInfoKey.智力成长:1.91,
# HeroInfoKey.初始统帅:76,
# HeroInfoKey.统帅成长:1.45,
# HeroInfoKey.初始先攻:41,
# HeroInfoKey.先攻成长:1.32,
# HeroInfoKey.自带战法:Fitting_List_Enum.飞鸿戏海

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 钟繇_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.钟繇
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 16
        self.武力成长 = 0.21
        self.初始智力 = 81
        self.智力成长 = 1.91
        self.初始统帅 = 76
        self.统帅成长 = 1.45
        self.初始先攻 = 41
        self.先攻成长 = 1.32
        self.自带战法 = Fitting_List_Enum.飞鸿戏海
        self.缘分列表 = []
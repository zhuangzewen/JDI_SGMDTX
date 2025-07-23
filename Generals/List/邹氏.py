# HeroInfoKey.武将名称:HeroName.邹氏,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:16,
# HeroInfoKey.武力成长:0.25,
# HeroInfoKey.初始智力:94,
# HeroInfoKey.智力成长:1.85,
# HeroInfoKey.初始统帅:88,
# HeroInfoKey.统帅成长:1.65,
# HeroInfoKey.初始先攻:64,
# HeroInfoKey.先攻成长:1.73,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 邹氏_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.邹氏
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 0
        self.初始武力 = 16
        self.武力成长 = 0.25
        self.初始智力 = 94
        self.智力成长 = 1.85
        self.初始统帅 = 88
        self.统帅成长 = 1.65
        self.初始先攻 = 64
        self.先攻成长 = 1.73
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.顾盼生姿
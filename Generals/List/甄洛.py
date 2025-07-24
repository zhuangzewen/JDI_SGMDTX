# HeroInfoKey.武将名称:HeroName.甄洛,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:22,
# HeroInfoKey.武力成长:0.23,
# HeroInfoKey.初始智力:103,
# HeroInfoKey.智力成长:2.16,
# HeroInfoKey.初始统帅:103,
# HeroInfoKey.统帅成长:1.62,
# HeroInfoKey.初始先攻:56,
# HeroInfoKey.先攻成长:1.55,
# HeroInfoKey.自带战法:Fitting_List_Enum.流风回雪,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 甄洛_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.甄洛
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 22
        self.武力成长 = 0.23
        self.初始智力 = 103
        self.智力成长 = 2.16
        self.初始统帅 = 103
        self.统帅成长 = 1.62
        self.初始先攻 = 56
        self.先攻成长 = 1.55
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.流风回雪
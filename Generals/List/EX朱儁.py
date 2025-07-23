# HeroInfoKey.武将名称:HeroName.EX朱儁,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:82,
# HeroInfoKey.武力成长:1.90,
# HeroInfoKey.初始智力:99,
# HeroInfoKey.智力成长:2.21,
# HeroInfoKey.初始统帅:106,
# HeroInfoKey.统帅成长:2.12,
# HeroInfoKey.初始先攻:88,
# HeroInfoKey.先攻成长:1.67,
# HeroInfoKey.自带战法:Fitting_List_Enum.围师必阙

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX朱儁_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX朱儁
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 82
        self.武力成长 = 1.90
        self.初始智力 = 99
        self.智力成长 = 2.21
        self.初始统帅 = 106
        self.统帅成长 = 2.12
        self.初始先攻 = 88
        self.先攻成长 = 1.67
        self.自带战法 = Fitting_List_Enum.围师必阙
        self.缘分列表 = []
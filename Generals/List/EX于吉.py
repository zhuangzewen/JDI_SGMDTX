# HeroInfoKey.武将名称:HeroName.EX于吉,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:12,
# HeroInfoKey.武力成长:0.21,
# HeroInfoKey.初始智力:103,
# HeroInfoKey.智力成长:2.51,
# HeroInfoKey.初始统帅:74,
# HeroInfoKey.统帅成长:1.87,
# HeroInfoKey.初始先攻:86,
# HeroInfoKey.先攻成长:1.97,
# HeroInfoKey.自带战法:Fitting_List_Enum.风急雨晦

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX于吉_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX于吉
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 12
        self.武力成长 = 0.21
        self.初始智力 = 103
        self.智力成长 = 2.51
        self.初始统帅 = 74
        self.统帅成长 = 1.87
        self.初始先攻 = 86
        self.先攻成长 = 1.97
        self.自带战法 = Fitting_List_Enum.风急雨晦
        self.缘分列表 = []
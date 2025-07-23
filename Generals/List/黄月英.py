# HeroInfoKey.武将名称:HeroName.黄月英,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:35,
# HeroInfoKey.武力成长:1.0,
# HeroInfoKey.初始智力:95,
# HeroInfoKey.智力成长:2.4,
# HeroInfoKey.初始统帅:78,
# HeroInfoKey.统帅成长:1.8,
# HeroInfoKey.初始先攻:62,
# HeroInfoKey.先攻成长:1.3,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 黄月英_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.黄月英
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 35
        self.武力成长 = 1.0
        self.初始智力 = 95
        self.智力成长 = 2.4
        self.初始统帅 = 78
        self.统帅成长 = 1.8
        self.初始先攻 = 62
        self.先攻成长 = 1.3
        self.缘分列表 = []
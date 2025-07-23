# HeroInfoKey.武将名称:HeroName.董卓,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:88,
# HeroInfoKey.武力成长:1.9,
# HeroInfoKey.初始智力:82,
# HeroInfoKey.智力成长:1.8,
# HeroInfoKey.初始统帅:95,
# HeroInfoKey.统帅成长:2.2,
# HeroInfoKey.初始先攻:62,
# HeroInfoKey.先攻成长:1.3,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 董卓_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.董卓
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 88
        self.武力成长 = 1.9
        self.初始智力 = 82
        self.智力成长 = 1.8
        self.初始统帅 = 95
        self.统帅成长 = 2.2
        self.初始先攻 = 62
        self.先攻成长 = 1.3
        self.缘分列表 = []
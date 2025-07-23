# HeroInfoKey.武将名称:HeroName.文丑,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:98,
# HeroInfoKey.武力成长:2.3,
# HeroInfoKey.初始智力:55,
# HeroInfoKey.智力成长:1.2,
# HeroInfoKey.初始统帅:72,
# HeroInfoKey.统帅成长:1.6,
# HeroInfoKey.初始先攻:88,
# HeroInfoKey.先攻成长:2.0,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 文丑_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.文丑
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 98
        self.武力成长 = 2.3
        self.初始智力 = 55
        self.智力成长 = 1.2
        self.初始统帅 = 72
        self.统帅成长 = 1.6
        self.初始先攻 = 88
        self.先攻成长 = 2.0
        self.缘分列表 = []
# HeroInfoKey.武将名称:HeroName.文丑,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:108,
# HeroInfoKey.武力成长:2.40,
# HeroInfoKey.初始智力:45,
# HeroInfoKey.智力成长:0.67,
# HeroInfoKey.初始统帅:91,
# HeroInfoKey.统帅成长:1.68,
# HeroInfoKey.初始先攻:76,
# HeroInfoKey.先攻成长:2.40,
# HeroInfoKey.自带战法:交锋震威,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 文丑_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.文丑
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 108
        self.武力成长 = 2.40
        self.初始智力 = 45
        self.智力成长 = 0.67
        self.初始统帅 = 91
        self.统帅成长 = 1.68
        self.初始先攻 = 76
        self.先攻成长 = 2.40
        self.自带战法 = Fitting_List_Enum.交锋震威
        self.缘分列表 = []
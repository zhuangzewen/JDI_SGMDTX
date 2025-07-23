# HeroInfoKey.武将名称:HeroName.袁绍,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:75,
# HeroInfoKey.武力成长:1.6,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:2.0,
# HeroInfoKey.初始统帅:98,
# HeroInfoKey.统帅成长:2.3,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.4,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 袁绍_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.袁绍
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 75
        self.武力成长 = 1.6
        self.初始智力 = 85
        self.智力成长 = 2.0
        self.初始统帅 = 98
        self.统帅成长 = 2.3
        self.初始先攻 = 65
        self.先攻成长 = 1.4
        self.缘分列表 = []
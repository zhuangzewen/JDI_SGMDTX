# HeroInfoKey.武将名称:HeroName.于吉,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:25,
# HeroInfoKey.武力成长:0.8,
# HeroInfoKey.初始智力:105,
# HeroInfoKey.智力成长:2.6,
# HeroInfoKey.初始统帅:68,
# HeroInfoKey.统帅成长:1.5,
# HeroInfoKey.初始先攻:58,
# HeroInfoKey.先攻成长:1.2,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 于吉_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.于吉
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 25
        self.武力成长 = 0.8
        self.初始智力 = 105
        self.智力成长 = 2.6
        self.初始统帅 = 68
        self.统帅成长 = 1.5
        self.初始先攻 = 58
        self.先攻成长 = 1.2
        self.缘分列表 = []
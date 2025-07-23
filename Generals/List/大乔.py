# HeroInfoKey.武将名称:HeroName.大乔,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:35,
# HeroInfoKey.武力成长:1.0,
# HeroInfoKey.初始智力:88,
# HeroInfoKey.智力成长:2.2,
# HeroInfoKey.初始统帅:72,
# HeroInfoKey.统帅成长:1.6,
# HeroInfoKey.初始先攻:78,
# HeroInfoKey.先攻成长:1.8,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 大乔_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.大乔
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 35
        self.武力成长 = 1.0
        self.初始智力 = 88
        self.智力成长 = 2.2
        self.初始统帅 = 72
        self.统帅成长 = 1.6
        self.初始先攻 = 78
        self.先攻成长 = 1.8
        self.缘分列表 = []
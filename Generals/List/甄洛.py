# HeroInfoKey.武将名称:HeroName.甄洛,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:38,
# HeroInfoKey.武力成长:1.0,
# HeroInfoKey.初始智力:88,
# HeroInfoKey.智力成长:2.2,
# HeroInfoKey.初始统帅:75,
# HeroInfoKey.统帅成长:1.8,
# HeroInfoKey.初始先攻:72,
# HeroInfoKey.先攻成长:1.6,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 甄洛_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.甄洛
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 38
        self.武力成长 = 1.0
        self.初始智力 = 88
        self.智力成长 = 2.2
        self.初始统帅 = 75
        self.统帅成长 = 1.8
        self.初始先攻 = 72
        self.先攻成长 = 1.6
        self.缘分列表 = []
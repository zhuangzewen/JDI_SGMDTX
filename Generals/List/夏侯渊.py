# HeroInfoKey.武将名称:HeroName.夏侯渊,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:107,
# HeroInfoKey.武力成长:2.40,
# HeroInfoKey.初始智力:59,
# HeroInfoKey.智力成长:0.75,
# HeroInfoKey.初始统帅:101,
# HeroInfoKey.统帅成长:1.74,
# HeroInfoKey.初始先攻:94,
# HeroInfoKey.先攻成长:2.81,
# HeroInfoKey.自带战法:Fitting_List_Enum.神速奔袭,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 夏侯渊_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.夏侯渊
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 107
        self.武力成长 = 2.40
        self.初始智力 = 59
        self.智力成长 = 0.75
        self.初始统帅 = 101
        self.统帅成长 = 1.74
        self.初始先攻 = 94
        self.先攻成长 = 2.81
        self.自带战法 = Fitting_List_Enum.神速奔袭
        self.缘分列表 = []
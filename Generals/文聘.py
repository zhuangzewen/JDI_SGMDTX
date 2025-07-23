# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:81,
# HeroInfoKey.武力成长:0.28,
# HeroInfoKey.初始智力:73,
# HeroInfoKey.智力成长:1.70,
# HeroInfoKey.初始统帅:89,
# HeroInfoKey.统帅成长:1.50,
# HeroInfoKey.初始先攻:25,
# HeroInfoKey.先攻成长:1.84,
# HeroInfoKey.自带战法:Fitting_List_Enum.扼守荆江

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 文聘_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.文聘
        self.武将阵营 = Faction.魏
        self.武将兵种 =WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 81
        self.武力成长 = 0.28
        self.初始智力 = 73
        self.智力成长 = 1.70
        self.初始统帅 = 89
        self.统帅成长 = 1.50
        self.初始先攻 = 25
        self.先攻成长 = 1.84
        self.自带战法 = Fitting_List_Enum.扼守荆江
        self.缘分列表 = []
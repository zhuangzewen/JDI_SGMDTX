# HeroInfoKey.武将名称:HeroName.张春华,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:43,
# HeroInfoKey.武力成长:0.35,
# HeroInfoKey.初始智力:96,
# HeroInfoKey.智力成长:2.19,
# HeroInfoKey.初始统帅:93,
# HeroInfoKey.统帅成长:2.12,
# HeroInfoKey.初始先攻:69,
# HeroInfoKey.先攻成长:1.56,
# HeroInfoKey.自带战法:Fitting_List_Enum.荼蘼心计,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张春华_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张春华
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 0
        self.初始武力 = 43
        self.武力成长 = 0.35
        self.初始智力 = 96
        self.智力成长 = 2.19
        self.初始统帅 = 93
        self.统帅成长 = 2.12
        self.初始先攻 = 69
        self.先攻成长 = 1.56
        self.自带战法 = Fitting_List_Enum.荼蘼心计
        self.缘分列表 = []
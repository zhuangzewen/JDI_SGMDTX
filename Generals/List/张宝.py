# HeroInfoKey.武将名称:HeroName.张宝,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:66,
# HeroInfoKey.武力成长:0.24,
# HeroInfoKey.初始智力:101,
# HeroInfoKey.智力成长:2.25,
# HeroInfoKey.初始统帅:99,
# HeroInfoKey.统帅成长:1.73,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.75,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张宝_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张宝
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 66
        self.武力成长 = 0.24
        self.初始智力 = 101
        self.智力成长 = 2.25
        self.初始统帅 = 99
        self.统帅成长 = 1.73
        self.初始先攻 = 65
        self.先攻成长 = 1.75
        self.自带战法 = Fitting_List_Enum.妖风大作
        self.缘分列表 = []
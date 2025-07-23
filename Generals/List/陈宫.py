# HeroInfoKey.武将名称:HeroName.陈宫,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:55,
# HeroInfoKey.武力成长:0.63,
# HeroInfoKey.初始智力:110,
# HeroInfoKey.智力成长:2.54,
# HeroInfoKey.初始统帅:86,
# HeroInfoKey.统帅成长:1.87,
# HeroInfoKey.初始先攻:73,
# HeroInfoKey.先攻成长:1.94,
# HeroInfoKey.自带战法:SkillName.智令从计

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 陈宫_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.陈宫
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 55
        self.武力成长 = 0.63
        self.初始智力 = 110
        self.智力成长 = 2.54
        self.初始统帅 = 86
        self.统帅成长 = 1.87
        self.初始先攻 = 73
        self.先攻成长 = 1.94
        self.自带战法 = Fitting_List_Enum.智令从计
        self.缘分列表 = []
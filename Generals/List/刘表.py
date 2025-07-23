
# HeroInfoKey.武将名称:HeroName.刘表,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:35,
# HeroInfoKey.武力成长:0.41,
# HeroInfoKey.初始智力:83,
# HeroInfoKey.智力成长:1.31,
# HeroInfoKey.初始统帅:54,
# HeroInfoKey.统帅成长:0.89,
# HeroInfoKey.初始先攻:41,
# HeroInfoKey.先攻成长:1.47,
# HeroInfoKey.自带战法:SkillName.跨蹈汉南

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 刘表_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.刘表
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 35
        self.武力成长 = 0.41
        self.初始智力 = 83
        self.智力成长 = 1.31
        self.初始统帅 = 54
        self.统帅成长 = 0.89
        self.初始先攻 = 41
        self.先攻成长 = 1.47
        self.自带战法 = Fitting_List_Enum.跨蹈汉南
        self.缘分列表 = []

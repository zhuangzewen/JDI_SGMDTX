
# HeroInfoKey.武将名称:Generals_Name_Enum.吕布,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:125,
# HeroInfoKey.武力成长:3.00,
# HeroInfoKey.初始智力:38,
# HeroInfoKey.智力成长:0.70,
# HeroInfoKey.初始统帅:93,
# HeroInfoKey.统帅成长:1.89,
# HeroInfoKey.初始先攻:76,
# HeroInfoKey.先攻成长:2.57,
# HeroInfoKey.自带战法:Fitting_List_Enum.骁勇无前

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 吕布_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.吕布
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 125
        self.武力成长 = 3.00
        self.初始智力 = 38
        self.智力成长 = 0.70
        self.初始统帅 = 93
        self.统帅成长 = 1.89
        self.初始先攻 = 76
        self.先攻成长 = 2.57
        self.自带战法 = Fitting_List_Enum.骁勇无前
# HeroInfoKey.武将名称:HeroName.EX袁术,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:76,
# HeroInfoKey.武力成长:1.86,
# HeroInfoKey.初始智力:89,
# HeroInfoKey.智力成长:1.83,
# HeroInfoKey.初始统帅:104,
# HeroInfoKey.统帅成长:2.18,
# HeroInfoKey.初始先攻:80,
# HeroInfoKey.先攻成长:1.91,
# HeroInfoKey.自带战法:Fitting_List_Enum.僭号天子

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX袁术_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX袁术
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 76
        self.武力成长 = 1.86
        self.初始智力 = 89
        self.智力成长 = 1.83
        self.初始统帅 = 104
        self.统帅成长 = 2.18
        self.初始先攻 = 80
        self.先攻成长 = 1.91
        self.自带战法 = Fitting_List_Enum.僭号天子
        self.缘分列表 = []
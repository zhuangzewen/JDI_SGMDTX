# HeroInfoKey.武将名称:HeroName.EX马腾,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:84,
# HeroInfoKey.武力成长:2.07,
# HeroInfoKey.初始智力:59,
# HeroInfoKey.智力成长:0.73,
# HeroInfoKey.初始统帅:101,
# HeroInfoKey.统帅成长:2.23,
# HeroInfoKey.初始先攻:91,
# HeroInfoKey.先攻成长:1.87,
# HeroInfoKey.自带战法:Fitting_List_Enum.雄踞西凉

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX马腾_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX马腾
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 84
        self.武力成长 = 2.07
        self.初始智力 = 59
        self.智力成长 = 0.73
        self.初始统帅 = 101
        self.统帅成长 = 2.23
        self.初始先攻 = 91
        self.先攻成长 = 1.87
        self.自带战法 = Fitting_List_Enum.雄踞西凉
        self.缘分列表 = []
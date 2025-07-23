# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:83,
# HeroInfoKey.武力成长:1.64,
# HeroInfoKey.初始智力:48,
# HeroInfoKey.智力成长:0.17,
# HeroInfoKey.初始统帅:81,
# HeroInfoKey.统帅成长:1.55,
# HeroInfoKey.初始先攻:63,
# HeroInfoKey.先攻成长:1.31,
# HeroInfoKey.自带战法:Fitting_List_Enum.江渚破敌

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 臧霸_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.臧霸
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 83
        self.武力成长 = 1.64
        self.初始智力 = 48
        self.智力成长 = 0.17
        self.初始统帅 = 81
        self.统帅成长 = 1.55
        self.初始先攻 = 63
        self.先攻成长 = 1.31
        self.自带战法 = Fitting_List_Enum.江渚破敌
        self.缘分列表 = []
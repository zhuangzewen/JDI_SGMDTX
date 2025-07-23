# HeroInfoKey.武将名称:HeroName.徐晃,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:95,
# HeroInfoKey.武力成长:2.2,
# HeroInfoKey.初始智力:75,
# HeroInfoKey.智力成长:1.6,
# HeroInfoKey.初始统帅:90,
# HeroInfoKey.统帅成长:2.0,
# HeroInfoKey.初始先攻:80,
# HeroInfoKey.先攻成长:1.7,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 徐晃_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.徐晃
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 95
        self.武力成长 = 2.2
        self.初始智力 = 75
        self.智力成长 = 1.6
        self.初始统帅 = 90
        self.统帅成长 = 2.0
        self.初始先攻 = 80
        self.先攻成长 = 1.7
        self.缘分列表 = []
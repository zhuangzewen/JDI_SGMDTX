# HeroInfoKey.武将名称:HeroName.李儒,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:27,
# HeroInfoKey.武力成长:0.35,
# HeroInfoKey.初始智力:105,
# HeroInfoKey.智力成长:2.48,
# HeroInfoKey.初始统帅:88,
# HeroInfoKey.统帅成长:1.48,
# HeroInfoKey.初始先攻:60,
# HeroInfoKey.先攻成长:1.99,
# HeroInfoKey.自带战法:Fitting_List_Enum.鸩饮毒弑

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 李儒_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.李儒
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 27
        self.武力成长 = 0.35
        self.初始智力 = 105
        self.智力成长 = 2.48
        self.初始统帅 = 88
        self.统帅成长 = 1.48
        self.初始先攻 = 60
        self.先攻成长 = 1.99
        self.自带战法 = Fitting_List_Enum.鸩饮毒弑
        self.缘分列表 = []
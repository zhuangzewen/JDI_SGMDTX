# HeroInfoKey.武将名称:HeroName.公孙瓒,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:99,
# HeroInfoKey.武力成长:2.01,
# HeroInfoKey.初始智力:86,
# HeroInfoKey.智力成长:1.91,
# HeroInfoKey.初始统帅:103,
# HeroInfoKey.统帅成长:1.90,
# HeroInfoKey.初始先攻:96,
# HeroInfoKey.先攻成长:2.30,
# HeroInfoKey.自带战法:威震塞外,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 公孙瓒_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.公孙瓒
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 99
        self.武力成长 = 2.01
        self.初始智力 = 86
        self.智力成长 = 1.91
        self.初始统帅 = 103
        self.统帅成长 = 1.90
        self.初始先攻 = 96
        self.先攻成长 = 2.30
        self.缘分列表 = []
        self.自带战法 = "威震塞外"
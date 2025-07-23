# HeroInfoKey.武将名称:HeroName.张角,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:35,
# HeroInfoKey.武力成长:0.43,
# HeroInfoKey.初始智力:113,
# HeroInfoKey.智力成长:2.55,
# HeroInfoKey.初始统帅:105,
# HeroInfoKey.统帅成长:1.99,
# HeroInfoKey.初始先攻:62,
# HeroInfoKey.先攻成长:1.53,
# HeroInfoKey.自带战法:黄天当立,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张角_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张角
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 35
        self.武力成长 = 0.43
        self.初始智力 = 113
        self.智力成长 = 2.55
        self.初始统帅 = 105
        self.统帅成长 = 1.99
        self.初始先攻 = 62
        self.先攻成长 = 1.53
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.黄天当立
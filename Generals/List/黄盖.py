# HeroInfoKey.武将名称:HeroName.黄盖,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:88,
# HeroInfoKey.武力成长:1.9,
# HeroInfoKey.初始智力:75,
# HeroInfoKey.智力成长:1.6,
# HeroInfoKey.初始统帅:92,
# HeroInfoKey.统帅成长:2.1,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.5,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 黄盖_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.黄盖
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 88
        self.武力成长 = 1.9
        self.初始智力 = 75
        self.智力成长 = 1.6
        self.初始统帅 = 92
        self.统帅成长 = 2.1
        self.初始先攻 = 65
        self.先攻成长 = 1.5
        self.缘分列表 = []

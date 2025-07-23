# HeroInfoKey.武将名称:HeroName.邓艾,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:88,
# HeroInfoKey.武力成长:1.9,
# HeroInfoKey.初始智力:95,
# HeroInfoKey.智力成长:2.4,
# HeroInfoKey.初始统帅:105,
# HeroInfoKey.统帅成长:2.5,
# HeroInfoKey.初始先攻:70,
# HeroInfoKey.先攻成长:1.6,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 邓艾_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.邓艾
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 88
        self.武力成长 = 1.9
        self.初始智力 = 95
        self.智力成长 = 2.4
        self.初始统帅 = 105
        self.统帅成长 = 2.5
        self.初始先攻 = 70
        self.先攻成长 = 1.6
        self.缘分列表 = []

# HeroInfoKey.武将名称:HeroName.董卓,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:101,
# HeroInfoKey.武力成长:2.20,
# HeroInfoKey.初始智力:87,
# HeroInfoKey.智力成长:1.42,
# HeroInfoKey.初始统帅:110,
# HeroInfoKey.统帅成长:2.10,
# HeroInfoKey.初始先攻:85,
# HeroInfoKey.先攻成长:1.93,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 董卓_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.董卓
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 101
        self.武力成长 = 2.20
        self.初始智力 = 87
        self.智力成长 = 1.42
        self.初始统帅 = 110
        self.统帅成长 = 2.10
        self.初始先攻 = 85
        self.先攻成长 = 1.93
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.权倾朝野
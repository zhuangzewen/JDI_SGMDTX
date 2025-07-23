# HeroInfoKey.武将名称:HeroName.周仓,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:92,
# HeroInfoKey.武力成长:2.1,
# HeroInfoKey.初始智力:45,
# HeroInfoKey.智力成长:1.0,
# HeroInfoKey.初始统帅:72,
# HeroInfoKey.统帅成长:1.6,
# HeroInfoKey.初始先攻:68,
# HeroInfoKey.先攻成长:1.4,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 周仓_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.周仓
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 92
        self.武力成长 = 2.1
        self.初始智力 = 45
        self.智力成长 = 1.0
        self.初始统帅 = 72
        self.统帅成长 = 1.6
        self.初始先攻 = 68
        self.先攻成长 = 1.4
        self.缘分列表 = []
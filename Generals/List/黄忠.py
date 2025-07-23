# HeroInfoKey.武将名称:HeroName.黄忠,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:98,
# HeroInfoKey.武力成长:2.3,
# HeroInfoKey.初始智力:68,
# HeroInfoKey.智力成长:1.5,
# HeroInfoKey.初始统帅:82,
# HeroInfoKey.统帅成长:1.8,
# HeroInfoKey.初始先攻:75,
# HeroInfoKey.先攻成长:1.6,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 黄忠_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.黄忠
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 98
        self.武力成长 = 2.3
        self.初始智力 = 68
        self.智力成长 = 1.5
        self.初始统帅 = 82
        self.统帅成长 = 1.8
        self.初始先攻 = 75
        self.先攻成长 = 1.6
        self.缘分列表 = []
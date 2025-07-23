# HeroInfoKey.武将名称:HeroName.庞统,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:48,
# HeroInfoKey.武力成长:1.1,
# HeroInfoKey.初始智力:105,
# HeroInfoKey.智力成长:2.6,
# HeroInfoKey.初始统帅:85,
# HeroInfoKey.统帅成长:2.0,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.4,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 庞统_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.庞统
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 48
        self.武力成长 = 1.1
        self.初始智力 = 105
        self.智力成长 = 2.6
        self.初始统帅 = 85
        self.统帅成长 = 2.0
        self.初始先攻 = 65
        self.先攻成长 = 1.4
        self.缘分列表 = []
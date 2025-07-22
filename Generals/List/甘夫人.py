# HeroInfoKey.武将名称:Generals_Name_Enum.甘夫人,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:25,
# HeroInfoKey.武力成长:0.29,
# HeroInfoKey.初始智力:102,
# HeroInfoKey.智力成长:1.95,
# HeroInfoKey.初始统帅:106,
# HeroInfoKey.统帅成长:1.62,
# HeroInfoKey.初始先攻:90,
# HeroInfoKey.先攻成长:1.68,
# HeroInfoKey.自带战法:Fitting_List_Enum.皇思淑仁

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 甘夫人_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.甘夫人
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 2
        self.初始武力 = 45
        self.武力成长 = 0.7
        self.初始智力 = 88
        self.智力成长 = 2.0
        self.初始统帅 = 72
        self.统帅成长 = 1.5
        self.初始先攻 = 50
        self.先攻成长 = 1.68
        self.自带战法 = Fitting_List_Enum.皇思淑仁
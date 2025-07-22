# HeroInfoKey.武将名称:Generals_Name_Enum.姜维,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:101,
# HeroInfoKey.武力成长:2.39,
# HeroInfoKey.初始智力:111,
# HeroInfoKey.智力成长:2.52,
# HeroInfoKey.初始统帅:91,
# HeroInfoKey.统帅成长:2.01,
# HeroInfoKey.初始先攻:76,
# HeroInfoKey.先攻成长:1.99,
# HeroInfoKey.自带战法:Fitting_List_Enum.九伐中原

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 姜维_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.姜维
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 92
        self.武力成长 = 2.0
        self.初始智力 = 90
        self.智力成长 = 2.2
        self.初始统帅 = 95
        self.统帅成长 = 2.1
        self.初始先攻 = 65
        self.先攻成长 = 1.99
        self.自带战法 = Fitting_List_Enum.九伐中原
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:42,
# HeroInfoKey.武力成长:0.45,
# HeroInfoKey.初始智力:91,
# HeroInfoKey.智力成长:1.82,
# HeroInfoKey.初始统帅:71,
# HeroInfoKey.统帅成长:1.48,
# HeroInfoKey.初始先攻:62,
# HeroInfoKey.先攻成长:1.34,
# HeroInfoKey.自带战法:Fitting_List_Enum.才器过人

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 马谡_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.马谡
        self.武将阵营 = Faction.蜀
        self.武将兵种 =WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 42
        self.武力成长 = 0.45
        self.初始智力 = 91
        self.智力成长 = 1.82
        self.初始统帅 = 71
        self.统帅成长 = 1.48
        self.初始先攻 = 62
        self.先攻成长 = 1.34
        self.自带战法 = Fitting_List_Enum.才器过人
        self.缘分列表 = []
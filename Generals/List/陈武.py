# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:89,
# HeroInfoKey.武力成长:1.77,
# HeroInfoKey.初始智力:49,
# HeroInfoKey.智力成长:0.58,
# HeroInfoKey.初始统帅:99,
# HeroInfoKey.统帅成长:1.55,
# HeroInfoKey.初始先攻:47,
# HeroInfoKey.先攻成长:1.39,
# HeroInfoKey.自带战法:Fitting_List_Enum.悍战无畏

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 陈武_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.陈武
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 89
        self.武力成长 = 1.77
        self.初始智力 = 49
        self.智力成长 = 0.58
        self.初始统帅 = 99
        self.统帅成长 = 1.55
        self.初始先攻 = 47
        self.先攻成长 = 1.39
        self.自带战法 = Fitting_List_Enum.悍战无畏
        self.缘分列表 = []
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.谋,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:24,
# HeroInfoKey.武力成长:0.44,
# HeroInfoKey.初始智力:90,
# HeroInfoKey.智力成长:1.75,
# HeroInfoKey.初始统帅:82,
# HeroInfoKey.统帅成长:1.49,
# HeroInfoKey.初始先攻:54,
# HeroInfoKey.先攻成长:1.34,
# HeroInfoKey.自带战法:Fitting_List_Enum.白眉良名

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 马良_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.马良
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 24
        self.武力成长 = 0.44
        self.初始智力 = 90
        self.智力成长 = 1.75
        self.初始统帅 = 82
        self.统帅成长 = 1.49
        self.初始先攻 = 54
        self.先攻成长 = 1.34
        self.自带战法 = Fitting_List_Enum.白眉良名
        self.缘分列表 = []
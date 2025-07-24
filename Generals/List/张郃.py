# HeroInfoKey.武将名称:HeroName.张郃,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:104,
# HeroInfoKey.武力成长:2.59,
# HeroInfoKey.初始智力:81,
# HeroInfoKey.智力成长:0.77,
# HeroInfoKey.初始统帅:101,
# HeroInfoKey.统帅成长:1.91,
# HeroInfoKey.初始先攻:67,
# HeroInfoKey.先攻成长:1.93,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张郃_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张郃
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 104
        self.武力成长 = 2.59
        self.初始智力 = 81
        self.智力成长 = 0.77
        self.初始统帅 = 101
        self.统帅成长 = 1.91
        self.初始先攻 = 67
        self.先攻成长 = 1.93
        self.缘分列表 = []
        self.自带战法 = [Fitting_List_Enum.大破街亭]
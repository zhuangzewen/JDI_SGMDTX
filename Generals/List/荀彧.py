# HeroInfoKey.武将名称:HeroName.荀彧,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:37,
# HeroInfoKey.武力成长:0.19,
# HeroInfoKey.初始智力:120,
# HeroInfoKey.智力成长:2.70,
# HeroInfoKey.初始统帅:78,
# HeroInfoKey.统帅成长:1.60,
# HeroInfoKey.初始先攻:57,
# HeroInfoKey.先攻成长:1.65,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 荀彧_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.荀彧
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 37
        self.武力成长 = 0.19
        self.初始智力 = 120
        self.智力成长 = 2.70
        self.初始统帅 = 78
        self.统帅成长 = 1.60
        self.初始先攻 = 57
        self.先攻成长 = 1.65
        self.自带战法 = Fitting_List_Enum.建计举人
        self.缘分列表 = []
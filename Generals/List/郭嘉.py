# HeroInfoKey.武将名称:HeroName.郭嘉,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:36,
# HeroInfoKey.武力成长:0.21,
# HeroInfoKey.初始智力:118,
# HeroInfoKey.智力成长:2.74,
# HeroInfoKey.初始统帅:92,
# HeroInfoKey.统帅成长:1.70,
# HeroInfoKey.初始先攻:53,
# HeroInfoKey.先攻成长:1.81,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 郭嘉_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.郭嘉
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 36
        self.武力成长 = 0.21
        self.初始智力 = 118
        self.智力成长 = 2.74
        self.初始统帅 = 92
        self.统帅成长 = 1.70
        self.初始先攻 = 53
        self.先攻成长 = 1.81
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.算无遗策
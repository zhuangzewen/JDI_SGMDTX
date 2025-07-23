# HeroInfoKey.武将名称:HeroName.庞德,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:106,
# HeroInfoKey.武力成长:2.40,
# HeroInfoKey.初始智力:71,
# HeroInfoKey.智力成长:0.78,
# HeroInfoKey.初始统帅:93,
# HeroInfoKey.统帅成长:1.69,
# HeroInfoKey.初始先攻:73,
# HeroInfoKey.先攻成长:2.69,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 庞德_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.庞德
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 106
        self.武力成长 = 2.40
        self.初始智力 = 71
        self.智力成长 = 0.78
        self.初始统帅 = 93
        self.统帅成长 = 1.69
        self.初始先攻 = 73
        self.先攻成长 = 2.69
        self.自带战法 = Fitting_List_Enum.陷阵踏难
        self.缘分列表 = []
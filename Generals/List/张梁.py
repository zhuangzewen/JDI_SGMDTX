# HeroInfoKey.武将名称:HeroName.张梁,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:105,
# HeroInfoKey.武力成长:2.15,
# HeroInfoKey.初始智力:47,
# HeroInfoKey.智力成长:0.51,
# HeroInfoKey.初始统帅:109,
# HeroInfoKey.统帅成长:1.98,
# HeroInfoKey.初始先攻:73,
# HeroInfoKey.先攻成长:2.08,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张梁_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张梁
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 105
        self.武力成长 = 2.15
        self.初始智力 = 47
        self.智力成长 = 0.51
        self.初始统帅 = 109
        self.统帅成长 = 1.98
        self.初始先攻 = 73
        self.先攻成长 = 2.08
        self.缘分列表 = []
        self.自带战法 = [Fitting_List_Enum.妖武]
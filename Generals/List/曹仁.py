# HeroInfoKey.武将名称:HeroName.曹仁,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:85,
# HeroInfoKey.武力成长:1.8,
# HeroInfoKey.初始智力:70,
# HeroInfoKey.智力成长:1.5,
# HeroInfoKey.初始统帅:95,
# HeroInfoKey.统帅成长:2.2,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.4,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 曹仁_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.曹仁
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 85
        self.武力成长 = 1.8
        self.初始智力 = 70
        self.智力成长 = 1.5
        self.初始统帅 = 95
        self.统帅成长 = 2.2
        self.初始先攻 = 65
        self.先攻成长 = 1.4
        self.缘分列表 = []
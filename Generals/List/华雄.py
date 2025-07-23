# HeroInfoKey.武将名称:HeroName.华雄,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:102,
# HeroInfoKey.武力成长:2.4,
# HeroInfoKey.初始智力:48,
# HeroInfoKey.智力成长:1.1,
# HeroInfoKey.初始统帅:75,
# HeroInfoKey.统帅成长:1.6,
# HeroInfoKey.初始先攻:82,
# HeroInfoKey.先攻成长:1.8,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 华雄_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.华雄
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 102
        self.武力成长 = 2.4
        self.初始智力 = 48
        self.智力成长 = 1.1
        self.初始统帅 = 75
        self.统帅成长 = 1.6
        self.初始先攻 = 82
        self.先攻成长 = 1.8
        self.缘分列表 = []
# HeroInfoKey.武将名称:HeroName.皇甫嵩,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:92,
# HeroInfoKey.武力成长:2.1,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:2.0,
# HeroInfoKey.初始统帅:102,
# HeroInfoKey.统帅成长:2.4,
# HeroInfoKey.初始先攻:75,
# HeroInfoKey.先攻成长:1.6,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 皇甫嵩_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.皇甫嵩
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 92
        self.武力成长 = 2.1
        self.初始智力 = 85
        self.智力成长 = 2.0
        self.初始统帅 = 102
        self.统帅成长 = 2.4
        self.初始先攻 = 75
        self.先攻成长 = 1.6
        self.缘分列表 = []
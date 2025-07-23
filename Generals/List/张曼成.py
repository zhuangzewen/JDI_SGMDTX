# HeroInfoKey.武将名称:HeroName.张曼成,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:85,
# HeroInfoKey.武力成长:1.55,
# HeroInfoKey.初始智力:23,
# HeroInfoKey.智力成长:0.28,
# HeroInfoKey.初始统帅:90,
# HeroInfoKey.统帅成长:1.70,
# HeroInfoKey.初始先攻:36,
# HeroInfoKey.先攻成长:1.39,
# HeroInfoKey.自带战法:SkillName.神上使

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张曼成_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张曼成
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 85
        self.武力成长 = 1.55
        self.初始智力 = 23
        self.智力成长 = 0.28
        self.初始统帅 = 90
        self.统帅成长 = 1.70
        self.初始先攻 = 36
        self.先攻成长 = 1.39
        self.自带战法 = Fitting_List_Enum.神上使
        self.缘分列表 = []
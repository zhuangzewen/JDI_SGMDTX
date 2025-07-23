# HeroInfoKey.武将名称:HeroName.卢植,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:60,
# HeroInfoKey.武力成长:0.55,
# HeroInfoKey.初始智力:87,
# HeroInfoKey.智力成长:1.72,
# HeroInfoKey.初始统帅:93,
# HeroInfoKey.统帅成长:1.75,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.31,
# HeroInfoKey.自带战法:SkillName.国之柱石

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 卢植_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.卢植
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 60
        self.武力成长 = 0.55
        self.初始智力 = 87
        self.智力成长 = 1.72
        self.初始统帅 = 93
        self.统帅成长 = 1.75
        self.初始先攻 = 65
        self.先攻成长 = 1.31
        self.自带战法 = Fitting_List_Enum.国之柱石
        self.缘分列表 = []  # TODO: 待补充卢植缘分关系
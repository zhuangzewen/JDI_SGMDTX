# HeroInfoKey.武将名称:HeroName.皇甫嵩,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:72,
# HeroInfoKey.武力成长:1.27,
# HeroInfoKey.初始智力:81,
# HeroInfoKey.智力成长:0.76,
# HeroInfoKey.初始统帅:93,
# HeroInfoKey.统帅成长:1.74,
# HeroInfoKey.初始先攻:23,
# HeroInfoKey.先攻成长:1.33,
# HeroInfoKey.自带战法:SkillName.平乱定叛

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 皇甫嵩_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.皇甫嵩
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 72
        self.武力成长 = 1.27
        self.初始智力 = 81
        self.智力成长 = 0.76
        self.初始统帅 = 93
        self.统帅成长 = 1.74
        self.初始先攻 = 23
        self.先攻成长 = 1.33
        self.自带战法 = Fitting_List_Enum.平乱定叛
        self.缘分列表 = []
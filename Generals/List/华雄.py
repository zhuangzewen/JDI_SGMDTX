# HeroInfoKey.武将名称:HeroName.华雄,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:105,
# HeroInfoKey.武力成长:2.39,
# HeroInfoKey.初始智力:43,
# HeroInfoKey.智力成长:0.65,
# HeroInfoKey.初始统帅:87,
# HeroInfoKey.统帅成长:1.79,
# HeroInfoKey.初始先攻:83,
# HeroInfoKey.先攻成长:2.48,
# HeroInfoKey.自带战法:SkillName.耀武扬威

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 华雄_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.华雄
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 105
        self.武力成长 = 2.39
        self.初始智力 = 43
        self.智力成长 = 0.65
        self.初始统帅 = 87
        self.统帅成长 = 1.79
        self.初始先攻 = 83
        self.先攻成长 = 2.48
        self.自带战法 = Fitting_List_Enum.耀武扬威
        self.缘分列表 = []
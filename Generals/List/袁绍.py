# HeroInfoKey.武将名称:HeroName.袁绍,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.初始武力:80,
# HeroInfoKey.武力成长:2.00,
# HeroInfoKey.初始智力:92,
# HeroInfoKey.智力成长:1.80,
# HeroInfoKey.初始统帅:105,
# HeroInfoKey.统帅成长:2.03,
# HeroInfoKey.初始先攻:68,
# HeroInfoKey.先攻成长:2.25,
# HeroInfoKey.自带战法:Fitting_List_Enum.合聚群雄,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 袁绍_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.袁绍
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 80
        self.武力成长 = 2.00
        self.初始智力 = 92
        self.智力成长 = 1.80
        self.初始统帅 = 105
        self.统帅成长 = 2.03
        self.初始先攻 = 68
        self.先攻成长 = 2.25
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.合聚群雄
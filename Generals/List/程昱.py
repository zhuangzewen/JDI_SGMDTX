# HeroInfoKey.武将名称:HeroName.程昱,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:47,
# HeroInfoKey.武力成长:0.57,
# HeroInfoKey.初始智力:111,
# HeroInfoKey.智力成长:2.46,
# HeroInfoKey.初始统帅:84,
# HeroInfoKey.统帅成长:1.73,
# HeroInfoKey.初始先攻:73,
# HeroInfoKey.先攻成长:2.24,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 程昱_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.程昱
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 47
        self.武力成长 = 0.57
        self.初始智力 = 111
        self.智力成长 = 2.46
        self.初始统帅 = 84
        self.统帅成长 = 1.73
        self.初始先攻 = 73
        self.先攻成长 = 2.24
        self.自带战法 = Fitting_List_Enum.勇冠贲育
        self.缘分列表 = []
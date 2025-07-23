# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:86,
# HeroInfoKey.武力成长:1.65,
# HeroInfoKey.初始智力:48,
# HeroInfoKey.智力成长:0.77,
# HeroInfoKey.初始统帅:82,
# HeroInfoKey.统帅成长:1.63,
# HeroInfoKey.初始先攻:54,
# HeroInfoKey.先攻成长:1.84,
# HeroInfoKey.自带战法:Fitting_List_Enum.八虎雄首

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 曹洪_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.曹洪
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 86
        self.武力成长 = 1.65
        self.初始智力 = 48
        self.智力成长 = 0.77
        self.初始统帅 = 82
        self.统帅成长 = 1.63
        self.初始先攻 = 54
        self.先攻成长 = 1.84
        self.自带战法 = Fitting_List_Enum.八虎雄首
        self.缘分列表 = []
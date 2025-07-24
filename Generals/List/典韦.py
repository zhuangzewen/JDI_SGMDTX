# HeroInfoKey.武将名称:HeroName.典韦,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:120,
# HeroInfoKey.武力成长:2.78,
# HeroInfoKey.初始智力:42,
# HeroInfoKey.智力成长:0.37,
# HeroInfoKey.初始统帅:114,
# HeroInfoKey.统帅成长:1.75,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:2.30,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 典韦_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.典韦
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 120
        self.武力成长 = 2.78
        self.初始智力 = 42
        self.智力成长 = 0.37
        self.初始统帅 = 114
        self.统帅成长 = 1.75
        self.初始先攻 = 65
        self.先攻成长 = 2.30
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.古之恶来
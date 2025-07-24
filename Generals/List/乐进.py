# HeroInfoKey.武将名称:HeroName.乐进,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:113,
# HeroInfoKey.武力成长:2.35,
# HeroInfoKey.初始智力:56,
# HeroInfoKey.智力成长:0.86,
# HeroInfoKey.初始统帅:104,
# HeroInfoKey.统帅成长:1.81,
# HeroInfoKey.初始先攻:92,
# HeroInfoKey.先攻成长:2.33,
# HeroInfoKey.自带战法:SkillName.每战先登,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 乐进_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.乐进
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 113
        self.武力成长 = 2.35
        self.初始智力 = 56
        self.智力成长 = 0.86
        self.初始统帅 = 104
        self.统帅成长 = 1.81
        self.初始先攻 = 92
        self.先攻成长 = 2.33
        self.自带战法 = Fitting_List_Enum.每战先登
        self.缘分列表 = []

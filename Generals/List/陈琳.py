# HeroInfoKey.武将名称:HeroName.陈琳,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:23,
# HeroInfoKey.武力成长:0.33,
# HeroInfoKey.初始智力:89,
# HeroInfoKey.智力成长:1.48,
# HeroInfoKey.初始统帅:61,
# HeroInfoKey.统帅成长:1.21,
# HeroInfoKey.初始先攻:34,
# HeroInfoKey.先攻成长:1.44,
# HeroInfoKey.自带战法:SkillName.讨贼檄文

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 陈琳_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.陈琳
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 23
        self.武力成长 = 0.33
        self.初始智力 = 89
        self.智力成长 = 1.48
        self.初始统帅 = 61
        self.统帅成长 = 1.21
        self.初始先攻 = 34
        self.先攻成长 = 1.44
        self.自带战法 = Fitting_List_Enum.讨贼檄文
        self.缘分列表 = []  # TODO: 待补充陈琳缘分关系
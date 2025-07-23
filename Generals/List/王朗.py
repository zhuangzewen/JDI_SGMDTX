
# HeroInfoKey.武将名称:HeroName.王朗,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:33,
# HeroInfoKey.武力成长:0.36,
# HeroInfoKey.初始智力:84,
# HeroInfoKey.智力成长:1.48,
# HeroInfoKey.初始统帅:45,
# HeroInfoKey.统帅成长:0.49,
# HeroInfoKey.初始先攻:63,
# HeroInfoKey.先攻成长:1.38,
# HeroInfoKey.自带战法:SkillName.高才博雅

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 王朗_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.王朗
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 33
        self.武力成长 = 0.36
        self.初始智力 = 84
        self.智力成长 = 1.48
        self.初始统帅 = 45
        self.统帅成长 = 0.49
        self.初始先攻 = 63
        self.先攻成长 = 1.38
        self.自带战法 = Fitting_List_Enum.高才博雅
        self.缘分列表 = []  # TODO: 待补充王朗缘分关系
# HeroInfoKey.武将名称:HeroName.郭图,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.谋略,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:51,
# HeroInfoKey.武力成长:0.57,
# HeroInfoKey.初始智力:84,
# HeroInfoKey.智力成长:1.60,
# HeroInfoKey.初始统帅:59,
# HeroInfoKey.统帅成长:1.38,
# HeroInfoKey.初始先攻:60,
# HeroInfoKey.先攻成长:1.39,
# HeroInfoKey.自带战法:SkillName.曲辞谄媚

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 郭图_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.郭图
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 51
        self.武力成长 = 0.57
        self.初始智力 = 84
        self.智力成长 = 1.60
        self.初始统帅 = 59
        self.统帅成长 = 1.38
        self.初始先攻 = 60
        self.先攻成长 = 1.39
        self.自带战法 = Fitting_List_Enum.曲辞谄媚
        self.缘分列表 = []  # TODO: 待补充郭图缘分关系
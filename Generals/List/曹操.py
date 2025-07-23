# HeroInfoKey.武将名称:HeroName.曹操,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:76,
# HeroInfoKey.武力成长:1.30,
# HeroInfoKey.初始智力:102,
# HeroInfoKey.智力成长:2.30,
# HeroInfoKey.初始统帅:107,
# HeroInfoKey.统帅成长:2.52,
# HeroInfoKey.初始先攻:53,
# HeroInfoKey.先攻成长:1.79,
# HeroInfoKey.自带战法:SkillName.乱世奸雄

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 曹操_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.曹操
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 76
        self.武力成长 = 1.30
        self.初始智力 = 102
        self.智力成长 = 2.30
        self.初始统帅 = 107
        self.统帅成长 = 2.52
        self.初始先攻 = 53
        self.先攻成长 = 1.79
        self.自带战法 = Fitting_List_Enum.乱世奸雄
        self.缘分列表 = [Fitting_List_Enum.三分天下]

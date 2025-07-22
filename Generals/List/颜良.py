
# HeroInfoKey.武将名称:HeroName.颜良,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:107,
# HeroInfoKey.武力成长:2.40,
# HeroInfoKey.初始智力:50,
# HeroInfoKey.智力成长:0.76,
# HeroInfoKey.初始统帅:92,
# HeroInfoKey.统帅成长:1.69,
# HeroInfoKey.初始先攻:77,
# HeroInfoKey.先攻成长:2.56,
# HeroInfoKey.自带战法:SkillName.膂力过人

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 颜良_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.颜良
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 107
        self.武力成长 = 2.40
        self.初始智力 = 50
        self.智力成长 = 0.76
        self.初始统帅 = 92
        self.统帅成长 = 1.69
        self.初始先攻 = 77
        self.先攻成长 = 2.56
        self.自带战法 = Fitting_List_Enum.膂力过人
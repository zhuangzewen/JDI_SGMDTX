# HeroInfoKey.武将名称:HeroName.司马懿,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:70,
# HeroInfoKey.武力成长:1.10,
# HeroInfoKey.初始智力:125,
# HeroInfoKey.智力成长:3.00,
# HeroInfoKey.初始统帅:110,
# HeroInfoKey.统帅成长:2.60,
# HeroInfoKey.初始先攻:75,
# HeroInfoKey.先攻成长:2.10,
# HeroInfoKey.自带战法:SkillName.鹰视狼顾

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 司马懿_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.司马懿
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 70
        self.武力成长 = 1.10
        self.初始智力 = 125
        self.智力成长 = 3.00
        self.初始统帅 = 110
        self.统帅成长 = 2.60
        self.初始先攻 = 75
        self.先攻成长 = 2.10
        self.自带战法 = Fitting_List_Enum.鹰视狼顾
        self.缘分列表 = [Fitting_List_Enum.魏武雄姿]

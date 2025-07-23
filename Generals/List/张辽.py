# HeroInfoKey.武将名称:HeroName.张辽,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:105,
# HeroInfoKey.武力成长:2.40,
# HeroInfoKey.初始智力:88,
# HeroInfoKey.智力成长:1.70,
# HeroInfoKey.初始统帅:92,
# HeroInfoKey.统帅成长:1.90,
# HeroInfoKey.初始先攻:80,
# HeroInfoKey.先攻成长:2.20,
# HeroInfoKey.自带战法:SkillName.逍遥津

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张辽_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张辽
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 105
        self.武力成长 = 2.40
        self.初始智力 = 88
        self.智力成长 = 1.70
        self.初始统帅 = 92
        self.统帅成长 = 1.90
        self.初始先攻 = 80
        self.先攻成长 = 2.20
        self.自带战法 = Fitting_List_Enum.逍遥津
        self.缘分列表 = [Fitting_List_Enum.魏武雄姿]

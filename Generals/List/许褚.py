
# HeroInfoKey.武将名称:HeroName.许褚,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:114,
# HeroInfoKey.武力成长:2.75,
# HeroInfoKey.初始智力:45,
# HeroInfoKey.智力成长:0.43,
# HeroInfoKey.初始统帅:95,
# HeroInfoKey.统帅成长:1.64,
# HeroInfoKey.初始先攻:69,
# HeroInfoKey.先攻成长:2.60,
# HeroInfoKey.自带战法:SkillName.裸衣血战

from Generals.JDI_Hero import HeroInfo
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum

class 许褚_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.许褚
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 114
        self.武力成长 = 2.75
        self.初始智力 = 45
        self.智力成长 = 0.43
        self.初始统帅 = 95
        self.统帅成长 = 1.64
        self.初始先攻 = 69
        self.先攻成长 = 2.60
        self.自带战法 = Fitting_List_Enum.裸衣血战


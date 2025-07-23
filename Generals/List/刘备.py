
# HeroInfoKey.武将名称:HeroName.刘备,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:80,
# HeroInfoKey.武力成长:1.43,
# HeroInfoKey.初始智力:94,
# HeroInfoKey.智力成长:2.31,
# HeroInfoKey.初始统帅:109,
# HeroInfoKey.统帅成长:2.12,
# HeroInfoKey.初始先攻:53,
# HeroInfoKey.先攻成长:1.72,
# HeroInfoKey.自带战法:SkillName.携民渡江

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 刘备_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.刘备
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 80
        self.武力成长 = 1.43
        self.初始智力 = 94
        self.智力成长 = 2.31
        self.初始统帅 = 109
        self.统帅成长 = 2.12
        self.初始先攻 = 53
        self.先攻成长 = 1.72
        self.自带战法 = Fitting_List_Enum.携民渡江
        self.缘分列表 = [Fitting_List_Enum.仁义昭烈]

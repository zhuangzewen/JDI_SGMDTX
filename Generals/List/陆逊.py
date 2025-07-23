# HeroInfoKey.武将名称:HeroName.陆逊,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:75,
# HeroInfoKey.武力成长:1.20,
# HeroInfoKey.初始智力:118,
# HeroInfoKey.智力成长:2.75,
# HeroInfoKey.初始统帅:108,
# HeroInfoKey.统帅成长:2.50,
# HeroInfoKey.初始先攻:78,
# HeroInfoKey.先攻成长:2.00,
# HeroInfoKey.自带战法:SkillName.火烧连营

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 陆逊_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.陆逊
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 75
        self.武力成长 = 1.20
        self.初始智力 = 118
        self.智力成长 = 2.75
        self.初始统帅 = 108
        self.统帅成长 = 2.50
        self.初始先攻 = 78
        self.先攻成长 = 2.00
        self.自带战法 = Fitting_List_Enum.火烧连营
        self.缘分列表 = []

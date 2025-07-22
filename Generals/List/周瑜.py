
# HeroInfoKey.武将名称:HeroName.周瑜,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:77,
# HeroInfoKey.武力成长:0.95,
# HeroInfoKey.初始智力:114,
# HeroInfoKey.智力成长:2.75,
# HeroInfoKey.初始统帅:104,
# HeroInfoKey.统帅成长:2.01,
# HeroInfoKey.初始先攻:62,
# HeroInfoKey.先攻成长:1.73,
# HeroInfoKey.自带战法:SkillName.临机制胜

from ._base import HeroInfo, Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 周瑜_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.周瑜
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 77
        self.武力成长 = 0.95
        self.初始智力 = 114
        self.智力成长 = 2.75
        self.初始统帅 = 104
        self.统帅成长 = 2.01
        self.初始先攻 = 62
        self.先攻成长 = 1.73
        self.自带战法 = Fitting_List_Enum.临机制胜

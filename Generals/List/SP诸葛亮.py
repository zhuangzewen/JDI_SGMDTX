
# HeroInfoKey.武将名称:HeroName.Sp_诸葛亮,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:53,
# HeroInfoKey.武力成长:0.56,
# HeroInfoKey.初始智力:125,
# HeroInfoKey.智力成长:3.00,
# HeroInfoKey.初始统帅:104,
# HeroInfoKey.统帅成长:2.24,
# HeroInfoKey.初始先攻:61,
# HeroInfoKey.先攻成长:1.71,
# HeroInfoKey.自带战法:SkillName.星罗棋布

from Generals.JDI_Hero import HeroInfo
from Generals.Enum.Generals_List_Enum import Generals_Name_Enum
from JDI_Enum import Faction, WeaponType, SkillName


class SP诸葛亮_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.SP诸葛亮
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 53
        self.武力成长 = 0.56
        self.初始智力 = 125
        self.智力成长 = 3.00
        self.初始统帅 = 104
        self.统帅成长 = 2.24
        self.初始先攻 = 61
        self.先攻成长 = 1.71
        self.自带战法 = SkillName.星罗棋布



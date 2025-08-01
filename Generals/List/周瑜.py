from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

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
        self.初始统率 = 104
        self.统率成长 = 2.01
        self.初始先攻 = 62
        self.先攻成长 = 1.73
        self.自带战法 = Fitting_List_Enum.临机制胜
        self.缘分列表 = [BondsName_Enum.顾曲唱和, BondsName_Enum.苦肉计, BondsName_Enum.国之栋梁, BondsName_Enum.东吴大都督]
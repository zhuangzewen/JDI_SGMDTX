from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum


class 凌统_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.凌统
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        
        # 初始属性
        self.初始武力 = 102
        self.初始智力 = 63
        self.初始统率 = 89
        self.初始先攻 = 90
        
        # 成长属性
        self.武力成长 = 2.18
        self.智力成长 = 0.88
        self.统率成长 = 1.42
        self.先攻成长 = 2.42
        
        # 战法
        self.自带战法 = Fitting_List_Enum.旋略勇进
        
        # 缘分
        self.缘分列表 = [BondsName_Enum.江表虎臣, BondsName_Enum.弯弓饮羽]
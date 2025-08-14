from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 张昭_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张昭
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        
        # 初始属性
        self.初始武力 = 16
        self.初始智力 = 103
        self.初始统率 = 83
        self.初始先攻 = 87
        
        # 成长属性
        self.武力成长 = 0.23
        self.智力成长 = 2.3
        self.统率成长 = 1.65
        self.先攻成长 = 1.79
        
        # 战法
        self.自带战法 = Fitting_List_Enum.直谏固政
        
        # 缘分
        self.缘分列表 = [BondsName_Enum.柱石之臣]
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 张辽_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张辽
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 115
        self.武力成长 = 2.55
        self.初始智力 = 92
        self.智力成长 = 1.49
        self.初始统率 = 103
        self.统率成长 = 1.95
        self.初始先攻 = 87
        self.先攻成长 = 2.61
        self.自带战法 = Fitting_List_Enum.风袭逍遥
        self.缘分列表 = [BondsName_Enum.骁龙飞将, BondsName_Enum.五子良将]
from hero_imports import *

class 乐进_info(HeroInfo):
    def __init__(self):
        super().__init__()
        self.武将名称 = Generals_Name_Enum.乐进
        self.阵营 = 阵营.魏
        self.兵种 = 兵种.枪
        self.性别 = 性别.男
        
        # 初始属性
        self.初始武力 = 113
        self.初始智力 = 56
        self.初始统帅 = 104
        self.初始先攻 = 92
        
        # 成长属性
        self.成长武力 = 2.35
        self.成长智力 = 0.86
        self.成长统帅 = 1.81
        self.成长先攻 = 2.33
        
        # 自带战法
        self.自带战法 = Fitting_List_Enum.每战先登
        
        # 缘分列表
        self.缘分列表 = [BondsName_Enum.五子良将]
from hero_imports import *

class 左慈_info(HeroInfo):
    def __init__(self):
        super().__init__()
        self.武将名称 = Generals_Name_Enum.左慈
        self.阵营 = 阵营.群
        self.兵种 = 兵种.盾
        self.性别 = 性别.男
        
        # 初始属性
        self.初始武力 = 14
        self.初始智力 = 112
        self.初始统帅 = 88
        self.初始先攻 = 63
        
        # 成长属性
        self.成长武力 = 0.34
        self.成长智力 = 2.65
        self.成长统帅 = 2.13
        self.成长先攻 = 1.77
        
        # 自带战法
        self.自带战法 = Fitting_List_Enum.云行雨施
        
        # 缘分列表
        self.缘分列表 = [BondsName_Enum.仙人抚顶, BondsName_Enum.道法自然]
        
        # 武将分类
        self.武将分类 = [武将分类.谋略, 武将分类.前排]
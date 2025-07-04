
# 战法名称: 星罗棋布
# 战法类型: 指挥
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 星罗棋布:
# 我军全体受到谋略伤害降低10%(受智力影响,对自身的效果提升30%),
# 战斗开始前施加星罗棋布,使阵型加成提升70%(受智力影响),并根据阵型类型获得棋局增益

# 棋局增益:
# 不同类型获得的棋局增益:
# 单前排阵型: 我军前排受到伤害降低12%(受智力影响),受击率固定为85%
# 双前排阵型: 我军统帅最低单体对前排造成伤害提升20%,每回合结束时对敌军随机1-2人造成160%伤害(伤害类型由武力或智力高的一项决定)
# 三前排阵型: 每个回合结束后我军智力最高单体对敌军全体造成60%谋略伤害(额外受全队累积治疗量影响)

from JDI_Skill import SkillInfo, Skill
from JDI_Enum import SkillName, SkillType, SkillFeature, WeaponType
from JDI_Enum import ResponseStatus
from JDI_Enum import SkillInfoKey

class 星罗棋布_info(SkillInfo):
    def __init__(self):
        self.战法名称 = SkillName.星罗棋布
        self.战法类型 = SkillType.指挥
        self.战法特性 = SkillFeature.辅助
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1
        self.战法响应时机列表 = [ResponseStatus.阵型结束, ResponseStatus.战法布阵开始, ResponseStatus.回合行动时, ResponseStatus.回合结束后]

class 星罗棋布_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def 星罗棋布_阵型强化系数(self):
        def 拟合过程数据统计():
            pass


        # 受 智力&升阶 影响, 原始值 0.7, 升阶 0.021
        # 言寺的函数拟合公式
        skill_info = getattr(self, SkillInfoKey.战法信息.value)
        skill_name = getattr(skill_info, SkillInfoKey.战法名称.value)
        rankUp = 0
        if hasattr(self.战法信息, SkillInfoKey.战法升阶.value):
            rankUp = getattr(self.战法信息, SkillInfoKey.战法升阶.value)

        if skill_name == SkillName.星罗棋布:
            from JDI_Hero import Hero
            original_value = 0.7 + rankUp * 0.021
            owner: Hero = self.get_持有者()
            x = owner.get_智力()
            y = 0.0019 * x - 0.1332 + original_value
            return y
        return 0
    
    def 星罗棋布_受到谋略伤害降低系数(self):
        def 拟合过程数据统计():
            pass

        # 受 智力&升阶 影响, 原始值 0.1, 升阶 0.003
        # 言寺的函数拟合公式
        skill_name = self.get_战法名称()
        rankUp = self.get_战法升阶()

        if skill_name == SkillName.星罗棋布:
            from JDI_Hero import Hero
            original_value = 0.1 + rankUp * 0.003
            owner: Hero = self.get_持有者()
            x = owner.get_智力()
            y = 0.000182 * x - 0.012145 + original_value
            return y
        return 0
    
    # 未拟合公式
    def 星罗棋布_单前排_受到伤害降低系数(self):
        def 拟合过程数据统计():
            pass

        # 受 智力 影响, 原始值 0.12
        skill_name = self.get_战法名称()
        if skill_name == SkillName.星罗棋布:
            from JDI_Hero import Hero
            original_value = 0.12
            owner: Hero = self.get_持有者()
            x = owner.get_智力()
            y = 0.000182 * x - 0.012145 + original_value
            return y
        return 0
    
    def 星罗棋布_双前排_对前排造成伤害提升系数(self):
        # 固定值 0.2
        skill_name = self.get_战法名称()
        if skill_name == SkillName.星罗棋布:
            original_value = 0.2
            return original_value
        return 0

# 战法名称: 草船借箭
# 战法类型: 指挥
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 草船借箭:
# 自身攻心提升24%,自身受到或造成伤害时,有50%概率对敌方随机单体造成80%谋略伤害,每回合可触发5次

# 满阶草船借箭:
# 自身攻心提升27.5%,自身受到或造成伤害时,有50%概率对敌方随机单体造成92%谋略伤害,每回合可触发5次

from JDI_Skill import SkillInfo, Skill
from JDI_Enum import SkillName, SkillType, SkillFeature, WeaponType, ResponseStatus

class 草船借箭_info(SkillInfo):
    def __init__(self):
        self.战法名称 = SkillName.草船借箭
        self.战法类型 = SkillType.指挥
        self.战法特性 = SkillFeature.谋略
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1
        self.战法响应时机列表 = [ResponseStatus.战法布阵开始, ResponseStatus.每回合重置阶段, ResponseStatus.造成伤害时, ResponseStatus.受到伤害时]

class 草船借箭_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)
        self.当前回合发动次数 = 0

    def 草船借箭_攻心提升系数(self):
        # 初始值为 24%
        # 每一级升阶提升基础初始值为 0.7%

        rankUp = self.get_战法升阶()
        value = 0.24 + rankUp * 0.007
        return value
    
    def 草船借箭_借箭伤害系数(self):
        # 初始值为 80%
        # 每一级升阶提升基础初始值为 2.4%

        rankUp = self.get_战法升阶()
        value = 0.8 + rankUp * 0.024
        return value
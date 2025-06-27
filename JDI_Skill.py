
from JDI_Enum import ResponseStatus, SkillType, SkillName, SkillInfoKey, HeroName, Faction, WeaponType, HeroInfoKey, Formation, SoulSourceType, SoulResponseTime, SoulEffectType, SimulatorMode

class SkillInfo():

    def __init__(self, skillname):
        self.inputName = skillname
        skills = {
            SkillName.星罗棋布 : {
                SkillInfoKey.战法名称 : SkillName.星罗棋布,
                SkillInfoKey.战法类型 : SkillType.指挥,
                SkillInfoKey.战法响应时机列表 : [ResponseStatus.阵型结束, ResponseStatus.战法布阵开始],
            },
        }

        if (skillname in skills):
            for keyName in skills[skillname]:
                if isinstance(keyName, SkillInfoKey):
                    keyStr = keyName.value
                    setattr(self, keyStr, skills[skillname][keyName])

class Skill():

    def __init__(self, hero, skillName):

        if hasattr(SkillName, skillName):
            skillInfo = SkillInfo(SkillName(skillName))
            setattr(self, SkillInfoKey.战法信息.value, skillInfo)
            setattr(self, SkillInfoKey.加载状态.value, True)
        else:
            setattr(self, SkillInfoKey.加载状态.value, False)

        setattr(self, SkillInfoKey.持有者.value, hero)

    def 战法信息(self):
        return getattr(self, SkillInfoKey.战法信息.value)

    def 加载状态(self):
        return getattr(self, SkillInfoKey.加载状态.value)
    
    def 战法类型(self):
        return getattr(self.战法信息, SkillInfoKey.战法类型.value)

    # 设置战法升阶
    def set_RankUp(self, value):
        setattr(self, SkillInfoKey.战法升阶.value, value)

    # 阵型增强系数
    def get_Strength_enhancement(self):
        skill_name = getattr(self.skillInfo, SkillInfoKey.战法名称.value)
        rankUp = 0
        if hasattr(self.skillInfo, SkillInfoKey.战法升阶.value):
            rankUp = getattr(self.skillInfo, SkillInfoKey.战法升阶.value)

        if skill_name == SkillName.星罗棋布:
            original_value = 0.7 + rankUp * 0.021
            x = getattr(self.owner, HeroInfoKey.智力.value)
            y = 0.0019 * x - 0.1332 + original_value
            return y
        return 0
    
    # 承受谋略伤害减少系数
    def get_Damage_reduction_strategy(self):
        skill_name = getattr(self.skillInfo, SkillInfoKey.战法名称.value)
        rankUp = 0
        if hasattr(self.skillInfo, SkillInfoKey.战法升阶.value):
            rankUp = getattr(self.skillInfo, SkillInfoKey.战法升阶.value)

        if skill_name == SkillName.星罗棋布:
            original_value = 0.1 + rankUp * 0.003
            x = getattr(self.owner, HeroInfoKey.智力.value)
            y = 0.000182 * x - 0.012145 + original_value
            return y
        return 0
    
    # 承受伤害减少系数
    def get_Damage_reduction(self):
        skill_name = getattr(self.skillInfo, SkillInfoKey.战法名称.value)
        rankUp = 0
        if hasattr(self.skillInfo, SkillInfoKey.战法升阶.value):
            rankUp = getattr(self.skillInfo, SkillInfoKey.战法升阶.value)

        if skill_name == SkillName.星罗棋布:
            x = getattr(self.owner, HeroInfoKey.智力.value)
            y = 0.000182 * x - 0.012145 + 0.12
            return y
        return 0
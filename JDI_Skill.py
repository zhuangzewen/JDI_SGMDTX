
from JDI_Enum import ResponseStatus, SkillType, SkillName, SkillInfoKey, HeroInfoKey
from JDI_Log import Log

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

    def get_战法信息(self):
        return getattr(self, SkillInfoKey.战法信息.value)

    def get_战法名称(self):
        if hasattr(self.get_战法信息(), SkillInfoKey.战法名称.value):
            return getattr(self.get_战法信息(), SkillInfoKey.战法名称.value)
        return None
    
    def get_战法响应时机列表(self):
        if hasattr(self.get_战法信息(), SkillInfoKey.战法响应时机列表.value):
            return getattr(self.get_战法信息(), SkillInfoKey.战法响应时机列表.value)
        return []
    
    def get_持有者(self):
        return getattr(self, SkillInfoKey.持有者.value)
    
    def get_战法升阶(self):
        if hasattr(self.get_战法信息(), SkillInfoKey.战法升阶.value):
            return getattr(self.get_战法信息(), SkillInfoKey.战法升阶.value)
        return 0
    
    def __init__(self, hero, skillName):

        if isinstance(skillName, SkillName):
            skillInfo = SkillInfo(SkillName(skillName))
            setattr(self, SkillInfoKey.战法信息.value, skillInfo)
            setattr(self, SkillInfoKey.加载状态.value, True)
            Log().show_debug_info('DEBUG------- 武将技能初始化完成'.format(skillName))
            Log().show_debug_info('DEBUG------- 武将技能信息: {}'.format(skillInfo.__dict__))

        else:
            setattr(self, SkillInfoKey.加载状态.value, False)
            Log().show_debug_info('DEBUG------- 武将技能初始化失败'.format(skillName))

        setattr(self, SkillInfoKey.持有者.value, hero)

    def 设置战法升阶(self, value):
        setattr(self, SkillInfoKey.战法升阶.value, value)
        Log().show_debug_info('DEBUG------- 设置战法升阶: {}'.format(value))
    
    def 加载状态(self):
        return getattr(self, SkillInfoKey.加载状态.value)

    def 战法信息(self):
        return getattr(self, SkillInfoKey.战法信息.value)
    
    def 战法类型(self):
        skill_info = getattr(self, SkillInfoKey.战法信息.value)
        if hasattr(skill_info, SkillInfoKey.战法类型.value):
            return getattr(skill_info, SkillInfoKey.战法类型.value)
        return None
    
    def 星罗棋布_阵型强化系数(self):
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
    
    def 星罗棋布_单前排_受到伤害降低系数(self):
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
        skill_name = self.get_战法名称()
        if skill_name == SkillName.星罗棋布:
            original_value = 0.2
            return original_value
        return 0

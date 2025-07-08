
from JDI_Enum import SkillName, SkillInfoKey

class SkillInfo():

    def __init__(self, skillname):
        self.inputName = skillname
        skills = {}
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
    
    def get_Soul_list(self):
        if hasattr(self, SkillInfoKey.Soul_list.value):
            return getattr(self, SkillInfoKey.Soul_list.value)
        return []

    def __init__(self, hero, skillName):

        if isinstance(skillName, SkillName):
            skillInfo = get_skill_info(skillName)
            setattr(self, SkillInfoKey.战法信息.value, skillInfo)
            setattr(self, SkillInfoKey.加载状态.value, True)

        else:
            setattr(self, SkillInfoKey.加载状态.value, False)

        setattr(self, SkillInfoKey.持有者.value, hero)
        setattr(self, SkillInfoKey.Soul_list.value, [])

    def fill_init_soul(self):
        pass

    def 设置战法升阶(self, value):
        setattr(self, SkillInfoKey.战法升阶.value, value)
    
    def 加载状态(self):
        return getattr(self, SkillInfoKey.加载状态.value)

    def 战法信息(self):
        return getattr(self, SkillInfoKey.战法信息.value)
    
    def 战法类型(self):
        skill_info = getattr(self, SkillInfoKey.战法信息.value)
        if hasattr(skill_info, SkillInfoKey.战法类型.value):
            return getattr(skill_info, SkillInfoKey.战法类型.value)
        return None

def get_skill_info(skillName):
    if skillName == SkillName.普攻:
        from External.Fitting.List.普攻 import 普攻_info
        skillInfo = 普攻_info()
    elif skillName == SkillName.星罗棋布:
        from External.Fitting.List.星罗棋布 import 星罗棋布_info
        skillInfo = 星罗棋布_info()
    elif skillName == SkillName.草船借箭:
        from External.Fitting.List.草船借箭 import 草船借箭_info
        skillInfo = 草船借箭_info()
    else:
        skillInfo = SkillInfo(skillName)
    return skillInfo

def get_skill(skillName, hero):
    if skillName == SkillName.普攻:
        from External.Fitting.List.普攻 import 普攻_skill
        skill = 普攻_skill(hero, skillName)
    elif skillName == SkillName.星罗棋布:
        from External.Fitting.List.星罗棋布 import 星罗棋布_skill
        skill = 星罗棋布_skill(hero, skillName)
    elif skillName == SkillName.草船借箭:
        from External.Fitting.List.草船借箭 import 草船借箭_skill
        skill = 草船借箭_skill(hero, skillName)
    else:
        skill = Skill(hero, skillName)
    return skill
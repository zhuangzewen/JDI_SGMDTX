
from External.Fitting.Enum.FittingInfoKey_Enum import SkillInfoKey
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from External.Bonds.Enum.BondsList_Enum import BondsName_Enum  # 导入BondsName_Enum

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

        if isinstance(skillName, (Fitting_List_Enum, BondsName_Enum)):  # 支持BondsName_Enum
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
    
    def get_战法类型(self):
        skill_info = getattr(self, SkillInfoKey.战法信息.value)
        if hasattr(skill_info, SkillInfoKey.战法类型.value):
            return getattr(skill_info, SkillInfoKey.战法类型.value)
        return None

def _get_skill_module(skillName):
    """
    通用的技能模块查找函数
    返回找到的模块，如果未找到则返回None
    """
    if not (isinstance(skillName, Fitting_List_Enum) or isinstance(skillName, BondsName_Enum)):  # 支持BondsName_Enum
        return None
    
    skill_name = skillName.value
    
    # 按优先级排序的搜索路径列表
    search_paths = [
        f"External.Fitting.List.{skill_name}",
        f"External.Fitting.List.自带战法.主动.{skill_name}",
        f"External.Fitting.List.自带战法.被动.{skill_name}",
        f"External.Fitting.List.自带战法.指挥.{skill_name}",
        f"External.Fitting.List.自带战法.追击.{skill_name}",
        f"External.Fitting.List.携带战法.主动.{skill_name}",
        f"External.Fitting.List.携带战法.被动.{skill_name}",
        f"External.Fitting.List.携带战法.指挥.{skill_name}",
        f"External.Fitting.List.携带战法.追击.{skill_name}",
        f"External.Bonds.List.{skill_name}",
    ]
    
    # 尝试每个路径，直到找到可用的模块
    for module_path in search_paths:
        try:
            import importlib
            module = importlib.import_module(module_path)
            return module
        except ImportError:
            continue
    
    return None


def get_skill_info(skillName):
    """
    动态获取技能信息，避免穷举
    使用约定优于配置的方式自动查找技能模块
    """
    if not (isinstance(skillName, Fitting_List_Enum) or isinstance(skillName, BondsName_Enum)):  # 支持BondsName_Enum
        return SkillInfo(skillName)
    
    skill_name = skillName.value
    module = _get_skill_module(skillName)
    
    if module:
        # 获取对应的info类
        info_class_name = f"{skill_name}_info"
        if hasattr(module, info_class_name):
            info_class = getattr(module, info_class_name)
            return info_class()
    
    # 如果模块未找到或没有对应的info类，返回默认的SkillInfo
    return SkillInfo(skillName)


def get_skill(skillName, hero):
    """
    动态获取技能实例，避免穷举
    使用约定优于配置的方式自动查找技能模块
    """
    if not (isinstance(skillName, Fitting_List_Enum) or isinstance(skillName, BondsName_Enum)):  # 支持BondsName_Enum
        return Skill(hero, skillName)
    
    skill_name = skillName.value
    module = _get_skill_module(skillName)
    
    if module:
        # 获取对应的skill类
        skill_class_name = f"{skill_name}_skill"
        if hasattr(module, skill_class_name):
            skill_class = getattr(module, skill_class_name)
            return skill_class(hero, skillName)
    
    # 如果模块未找到或没有对应的skill类，返回默认的Skill
    return Skill(hero, skillName)
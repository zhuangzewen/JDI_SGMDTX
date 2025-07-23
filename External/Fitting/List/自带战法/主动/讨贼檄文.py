from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, WeaponType, SkillFeature, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 讨贼檄文_info(BaseSkillInfo):
    def __init__(self):
        # 使用模板系统获取配置
        template = get_skill_template('主动_谋略', Fitting_List_Enum.讨贼檄文)
        super().__init__(template)

class 讨贼檄文_soul(BaseSkillSoul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill=skill)
        self.soul持有列表 = []

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.主动战法行动时 and hero == self.target:
            from External.Fitting.List.Abnormal.清醒 import 清醒_soul
            清醒soul = 清醒_soul(
                target=self.target,
                initiator=self.target,
                sourceType=SoulSourceType.武将战法,
                skill=self.skill,
                response_time=SoulResponseTime.内置待响应,
                duration=1,
                effect_type=SoulEffectType.清醒,
                effect_value=0,
                source_soul=self,
                battleField=battleField)
            
            if 清醒soul.initiator.get_被击溃状态() != True and 清醒soul.target.get_被击溃状态() != True:
                Log().battle_L2('[{}]执行来自【{}】的[讨贼檄文-清醒]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

            清醒soul.deploy_initial()
            self.soul持有列表.append(清醒soul)
            self.target.get_响应Soul列表().append(清醒soul)

class 讨贼檄文_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        讨贼檄文soul = 讨贼檄文_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            skill=self)
        self.get_Soul_list().append(讨贼檄文soul)
        self.get_持有者().get_持有Soul列表().append(讨贼檄文soul)
        self.get_持有者().get_响应Soul列表().append(讨贼檄文soul)

    def 讨贼檄文_发动率(self):
        # 初始值为 0.6
        # 每一级升阶提升基础初始值为 0.01
        rankUp = self.get_战法升阶()
        value = 0.6 + rankUp * 0.01
        return value
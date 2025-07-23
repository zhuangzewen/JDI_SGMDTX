
# 战法名称: 跨蹈汉南
# 战法类型: 主动
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.3

# 跨蹈汉南:
# 对敌军随机单体造成60%→67.7%谋略伤害

# 满阶跨蹈汉南:
# 对敌军随机单体造成67.7%谋略伤害

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, Fitting_List_Enum, Log
)

class 跨蹈汉南_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板
        template = get_skill_template('主动_谋略', Fitting_List_Enum.跨蹈汉南)
        super().__init__(template)
        self.战法描述 = "对敌军随机单体造成60%→67.7%谋略伤害"

class 跨蹈汉南_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.回合行动时:
            Log().battle_L1('[{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))
            
            # 谋略伤害效果
            soul = self.skill.create_soul(
                self.target, 
                SoulEffectType.谋略伤害, 
                self.skill.跨蹈汉南_伤害系数()
            )
            soul.deploy_initial()
            self.soul持有列表.append(soul)

class 跨蹈汉南_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        soul = 跨蹈汉南_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )

        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    def 跨蹈汉南_伤害系数(self):
        return self.get_rank_bonus(0.6, 0.0077)
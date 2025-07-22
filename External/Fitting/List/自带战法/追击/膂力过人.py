# 战法名称: 膂力过人
# 战法类型: 追击
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 膂力过人:
# 普通攻击后,对当前攻击目标造成150%兵刃伤害,若目标武力低于自身额外造成70%兵刃伤害

# 满阶膂力过人:
# 普通攻击后,对当前攻击目标造成172.5%兵刃伤害,若目标武力低于自身额外造成90.5%兵刃伤害

from External.Fitting.List.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log
)
from Calcu.JDI_Calculate import 计算伤害

class 膂力过人_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板
        template = get_skill_template('追击_兵刃', Fitting_List_Enum.膂力过人)
        super().__init__(template)

class 膂力过人_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.追击行动时 and self.target == hero:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))
            
            attacked_hero = sourceSoul.target
            
            # 基础伤害
            damage_soul = self.skill.create_damage_soul(
                battleField, self.target, attacked_hero, 
                SoulDamageType.兵刃, SkillType.追击, 
                self.skill.膂力过人_伤害系数(), self
            )
            damage_soul.deploy_initial()

            # 额外伤害判定
            if attacked_hero.get_武力() < self.target.get_武力():
                extra_damage_soul = self.skill.create_damage_soul(
                    battleField, self.target, attacked_hero,
                    SoulDamageType.兵刃, SkillType.追击,
                    self.skill.膂力过人_额外伤害系数(), self,
                    effect_name="膂力过人"
                )
                extra_damage_soul.deploy_initial()

class 膂力过人_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        # 使用基类的便捷方法创建Soul
        soul = 膂力过人_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            sourceType=SoulSourceType.武将战法, 
            skill=self, 
            response_time=SoulResponseTime.内置待响应, 
            effect_type=SoulEffectType.无影响
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    # 使用基类的便捷方法简化数值计算
    def 膂力过人_伤害系数(self):
        return self.get_rank_bonus(1.5, 0.045)
    
    def 膂力过人_额外伤害系数(self):
        return self.get_rank_bonus(0.7, 0.021)

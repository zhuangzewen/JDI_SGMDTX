# 战法名称: 裸衣血战 (使用模板系统重构版本)
# 战法类型: 被动
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 裸衣血战:
# 战斗开始时,自身先攻和武力提升20点,连击率提升100%,统率降低15点。自身造成伤害额外提升0%

# 满阶裸衣血战:
# 战斗开始时,自身先攻和武力提升22点,连击率提升100%,统率降低15点。自身造成伤害额外提升5%

from External.Fitting.List.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, Fitting_List_Enum, Log
)

class 裸衣血战_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板
        template = get_skill_template('被动_兵刃', Fitting_List_Enum.裸衣血战)
        super().__init__(template)

class 裸衣血战_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))
            
            # 使用基类的便捷方法创建多个效果
            effects = [
                (SoulEffectType.先攻, self.skill.裸衣血战_先攻_提升系数()),
                (SoulEffectType.武力, self.skill.裸衣血战_武力_提升系数()),
                (SoulEffectType.连击几率, self.skill.裸衣血战_连击率_提升系数()),
                (SoulEffectType.统帅, -self.skill.裸衣血战_统帅_降低系数()),
                (SoulEffectType.造成伤害, self.skill.裸衣血战_造成伤害_提升系数())
            ]
            
            for effect_type, value in effects:
                soul = self.skill.create_soul(self.target, effect_type, value)
                if effect_type == SoulEffectType.统帅:
                    soul.battleField = battleField
                soul.deploy_initial()
                self.soul持有列表.append(soul)

class 裸衣血战_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        # 使用基类的便捷方法创建Soul
        soul = 裸衣血战_soul(
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
    def 裸衣血战_先攻_提升系数(self):
        return self.get_rank_bonus(20, 0.4)
    
    def 裸衣血战_武力_提升系数(self):
        return self.get_rank_bonus(20, 0.4)
    
    def 裸衣血战_连击率_提升系数(self):
        return 1
    
    def 裸衣血战_统帅_降低系数(self):
        return 15
    
    def 裸衣血战_造成伤害_提升系数(self):
        return self.get_rank_bonus(0, 0.01)

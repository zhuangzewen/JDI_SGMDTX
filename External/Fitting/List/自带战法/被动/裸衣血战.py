# 战法名称: 裸衣血战
# 战法类型: 被动
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 裸衣血战:
# 战斗开始时,自身先攻和武力提升20点,连击率提升100%,统率降低15点。自身造成伤害额外提升0%

# 满阶裸衣血战:
# 战斗开始时,自身先攻和武力提升22点,连击率提升100%,统率降低15点。自身造成伤害额外提升5%

# 裸衣血战_soul
# 创建部署时机: 被动战法部署时
# target: 自身
# initiator: 自身
# 持有soul对象: 自身
# 响应soul对象: 自身
# 响应持续时间: 永久
# 响应各类驱散: 无
# 额外溃败影响: 无

# 裸衣血战_soul - soul持有列表
# 1. 裸衣血战_先攻soul
# 2. 裸衣血战_武力soul
# 3. 裸衣血战_连击率soul
# 4. 裸衣血战_统率soul
# 5. 裸衣血战_造成伤害提升soul
# 创建部署时机: 裸衣血战_soul部署时
# target: 自身
# initiator: 自身
# 持有soul对象: 无
# 响应soul对象: 无
# 响应持续时间: 永久
# 响应各类驱散: 无
# 额外溃败影响: 无

# 持续时间响应: 无

# 各类驱散响应: 无

# 额外溃败影响: 无

# 裸衣血战 溃败响应
# 移除响应soul对象:             裸衣血战_soul
# soul持有列表筛除target:       1~5
# soul持有列表重置initiator:    无存在
# soul持有列表筛除initiator:    无存在
# 移除持有soul对象:             裸衣血战_soul


from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, Fitting_List_Enum, Log,
    Soul, SkillType, SoulDamageType
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
            Log().battle_L1('[{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))
            
            # 使用基类的便捷方法创建多个效果
            effects = [
                (SoulEffectType.先攻, self.skill.裸衣血战_先攻_提升系数()),
                (SoulEffectType.武力, self.skill.裸衣血战_武力_提升系数()),
                (SoulEffectType.连击几率, self.skill.裸衣血战_连击率_提升系数()),
                (SoulEffectType.统率, -self.skill.裸衣血战_统率_降低系数()),
                (SoulEffectType.造成伤害提升, self.skill.裸衣血战_造成伤害_提升系数())
            ]
            
            for effect_type, value in effects:
                soul = Soul(
                    target=self.target,
                    initiator=self.target,
                    sourceType=SoulSourceType.武将战法,
                    skill=self.skill,
                    effect_type=effect_type,
                    effect_value=value
                )
                if effect_type == SoulEffectType.统率:
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
            skill=self
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
    
    def 裸衣血战_统率_降低系数(self):
        return 15
    
    def 裸衣血战_造成伤害_提升系数(self):
        return self.get_rank_bonus(0, 0.01)

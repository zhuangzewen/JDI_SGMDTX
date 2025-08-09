# 战法名称: 草船借箭
# 战法类型: 指挥
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 草船借箭:
# 自身攻心提升24%,自身受到或造成伤害时,有50%概率对敌方随机单体造成80%谋略伤害,每回合可触发5次

# 满阶草船借箭:
# 自身攻心提升27.5%,自身受到或造成伤害时,有50%概率对敌方随机单体造成92%谋略伤害,每回合可触发5次

from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, Hero, Soul, Skill
)
from Calcu.JDI_Calculate import *

class 草船借箭_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板
        template = get_skill_template('指挥_谋略', Fitting_List_Enum.草船借箭)
        super().__init__(template)

class 草船借箭_soul(BaseSkillSoul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero,
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)
        self.soul持有列表 = []
        self.草船借箭发动次数 = 0

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            self._deploy_攻心效果()

        elif status == SoulResponseTime.回合重置阶段:
            self.草船借箭发动次数 = 0

        elif status in [SoulResponseTime.造成伤害时, SoulResponseTime.受到伤害时]:
            if hero != self.target:
                return

            if self.草船借箭发动次数 < 5:
                self._try_trigger_借箭效果(battleField)
                pass

    def _deploy_攻心效果(self):
        Log().battle_L1('[{}]发动战法【{}】'.format(
            self.target.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))
        
        攻心soul = self.skill.create_soul(
            self.target, SoulEffectType.攻心, self.skill.草船借箭_攻心提升系数()
        )
        攻心soul.deploy_initial()
        self.soul持有列表.append(攻心soul)

    def _try_trigger_借箭效果(self, battleField):
        """尝试触发借箭效果的便捷方法"""
        if random.random() > 0.5:
            Log().debug_L2(f'[{self.target.get_武将名称().value}]发动来自【{self.skill.get_战法名称().value}】的[草船借箭]效果, 但因几率未触发')
            return
        
        Log().battle_L2('[{}]执行来自【{}】的[草船借箭]效果'.format(
            self.target.get_武将名称().value, self.skill.get_战法名称().value))

        self.草船借箭发动次数 += 1

        # 对敌方随机单体造成谋略伤害
        attacked_heroes = 对敌方所有目标生效(self.target, battleField)
        if len(attacked_heroes) > 0:
            attacked = 从队列确定受击单位(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            Log().battle_L1('[{}]执行来自【{}】的[{}]效果'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value, 
                '草船借箭'
            ))
            damage_soul = self.skill.create_damage_soul(
                battleField = battleField, 
                initiator = self.target,
                target = attacked, 
                damage_type = SoulDamageType.谋略, 
                skill_type = SkillType.指挥, 
                damage_multiplier = self.skill.草船借箭_借箭伤害系数(), 
                source_soul = self,
                effect_name = '草船借箭'
            )
            damage_soul.deploy_initial()

class 草船借箭_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        # 使用基类的便捷方法创建Soul
        soul = 草船借箭_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    # 使用基类的便捷方法简化数值计算
    def 草船借箭_攻心提升系数(self):
        return self.get_rank_bonus(0.24, 0.007)
    
    def 草船借箭_借箭伤害系数(self):
        return self.get_rank_bonus(0.8, 0.024)

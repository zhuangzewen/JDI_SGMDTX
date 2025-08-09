# 战法名称: 木牛流马
# 战法类型: 指挥
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 木牛流马:
# 奇数回合开始时提升我军全体25%造成伤害(受智力影响)，持续至回合结束。
# 偶数回合开始时恢复我军全体兵力(治疗率220%)

from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType,
    Fitting_List_Enum, Log, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 木牛流马_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('指挥_辅助', Fitting_List_Enum.木牛流马, 1.0)
        super().__init__(template)

class 木牛流马_增伤soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 initialTeam=None,
                 sourceType=None, 
                 sourceDetail=[],
                 skill=None, 
                 response_time=None, 
                 duration=1, 
                 effect_type=SoulEffectType.造成伤害提升, 
                 effect_value=0,
                 source_soul=None,
                 battleField=None,
                 damage=Damage(skillEffectName="木牛流马-决机")):
         super().__init__(target, initiator, initialTeam, sourceType, sourceDetail, skill, response_time, duration, effect_type, effect_value, source_soul, battleField, damage)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.回合结束重置阶段:
            self.restore_initial()

class 木牛流马_soul(BaseSkillSoul):

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.回合开始时:
            current_round = battleField.current_round
            if current_round % 2 == 1:  # 奇数回合
                self._deploy_增伤效果(battleField)
            else:  # 偶数回合
                self._deploy_治疗效果(battleField)

    def _deploy_增伤效果(self, battleField):
        Log().battle_L1('[{}]执行来自【{}】的[木牛流马]效果'.format(
            self.initiator.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)

        for 目标武将 in value_heroes:
            # 检查是否已有增伤效果，有则刷新，无则添加
            for 已存在soul in 目标武将.get_响应Soul列表():
                已存在soul: Soul
                if 已存在soul.source_soul == self and 已存在soul.effect_type == SoulEffectType.造成伤害提升:
                    已存在soul.duration = 1
                    Log().battle_L2('[{}]的[木牛流马]增伤效果已刷新'.format(目标武将.get_武将名称().value))
                    break
            else:
                增伤soul = 木牛流马_增伤soul(
                    target=目标武将,
                    initiator=self.initiator,
                    sourceType=SoulSourceType.武将战法,
                    skill=self.skill,
                    effect_value=self.skill.木牛流马_增伤系数计算(),
                    duration=-1,
                    source_soul=self,
                    battleField=battleField
                )
                增伤soul.deploy_initial()
                self.soul持有列表.append(增伤soul)
                目标武将.get_响应Soul列表().append(增伤soul)

    def _deploy_治疗效果(self, battleField):
        initiator = self.initiator

        Log().battle_L1('[{}]执行来自【{}】的[木牛流马]效果 - 治疗'.format(
            initiator.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)

        for 目标武将 in value_heroes:
            治疗soul = self.skill.create_soul(
                target=目标武将,
                effect_type=SoulEffectType.恢复兵力,
                effect_value=治疗计算(battleField, 施救者=self.target, 受助者=目标武将, 治疗率 = self.skill.木牛流马_治疗率计算())
            )
            治疗soul.deploy_initial()   

class 木牛流马_skill(BaseSkill):

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()

        # 使用基类的便捷方法创建Soul
        soul = 木牛流马_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )

        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)
        return soul

    def 木牛流马_增伤系数计算(self):
        return self.get_rank_bonus(0.25, 0.0075)

    def 木牛流马_治疗率计算(self):
        return self.get_rank_bonus(2.2, 0.066)
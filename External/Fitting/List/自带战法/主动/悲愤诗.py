# 战法名称: 悲愤诗
# 战法类型: 主动
# 战法特性: 治疗
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.6

# 悲愤诗:
# 恢复我军全体兵力(治疗率120%,受智力影响),并施加1层抵御。若目标为前排,则额外恢复兵力(治疗率50%,受智力影响)

from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType, Damage
)
from Calcu.JDI_Calculate import *
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Control.Imports.hero_imports import Fitting_List_Enum

class 悲愤诗_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('主动_治疗', Fitting_List_Enum.悲愤诗, 0.6)
        super().__init__(template)

class 悲愤诗_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.主动战法行动时 and hero == self.target:

            if not msg_主动战法发起判断(self.target):
                Log().battle_L0('[{}]战法【{}】无法释放'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return

            悲愤诗skill: 悲愤诗_skill = self.skill
            实际发动率 = (1 + self.target.get_主动战法发动率降低()) * 悲愤诗skill.悲愤诗_发动率()

            # 判断是否发动
            if random.random() > 实际发动率:
                Log().battle_L2('[{}]因几率未发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return
            self._deploy_heal_and_shield(battleField)
            pass

    def _deploy_heal_and_shield(self, battleField):
        Log().battle_L2('[{}]发动战法【{}】'.format(
            self.target.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)
        value_times = len(value_heroes)
        
        for _ in range(value_times):
            if len(value_heroes) == 0:
                break

            目标武将 = 从队列确定受击单位(value_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            全体治疗soul = self.skill.create_soul(
                target=目标武将,
                effect_type=SoulEffectType.恢复兵力,
                effect_value=治疗计算(battleField, 施救者=self.target, 受助者=目标武将, 治疗率 = self.skill.悲愤诗_基础治疗率())
            )
            全体治疗soul.deploy_initial()

            if 目标武将.get_前排状态() == True:
                额外治疗soul = self.skill.create_soul(
                    target=目标武将,
                    effect_type=SoulEffectType.恢复兵力,
                    effect_value=治疗计算(battleField, 施救者=self.target, 受助者=目标武将, 治疗率 = self.skill.悲愤诗_前排额外治疗率())
                )
                额外治疗soul.deploy_initial()

            Log().battle_L2('[{}]执行来自【悲愤诗】的「悲愤诗」效果'.format(目标武将.get_武将名称().value))

            抵御soul = self.skill.create_soul(
                target=目标武将,
                effect_type=SoulEffectType.抵御,
                effect_value=1,
                damage=Damage(skillEffectName='悲愤诗')
            )
            抵御soul.deploy_initial()

class 悲愤诗_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        soul = 悲愤诗_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            skill=self
        )
        self.get_持有者().get_响应Soul列表().append(soul)
        return soul

    def 悲愤诗_发动率(self):
        return 0.65

    def 悲愤诗_基础治疗率(self):
        return self.get_rank_bonus(1.2, 0.048)

    def 悲愤诗_前排额外治疗率(self):
        return self.get_rank_bonus(0.5, 0.02)

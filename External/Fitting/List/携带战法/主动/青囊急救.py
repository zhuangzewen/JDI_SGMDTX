# 战法名称: 青囊急救
# 战法类型: 主动
# 战法特性: 治疗
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.55

# 青囊急救:
# 驱散我军兵力最低单体3种负面状态，并恢复其兵力(治疗率260%)

from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType,
    Fitting_List_Enum, Log, random, Hero,
    Soul, SoulSourceType, SkillType, SoulDamageType
)
from Calcu.JDI_Calculate import *
from typing import List

class 青囊急救_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('主动_治疗', Fitting_List_Enum.青囊急救, 0.55)
        super().__init__(template)

class 青囊急救_soul(BaseSkillSoul):

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.主动战法行动时 and self.target == hero:
            # 55%发动率
            if random.random() > self.skill.get_发动率():
                Log().debug_L2(f'[{self.target.get_武将名称().value}]发动来自【{self.skill.get_战法名称().value}】的[青囊急救]效果, 但因几率未触发')
                return

            Log().battle_L1('[{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value     
            ))

            self._deploy_治疗效果(battleField)

    def _deploy_治疗效果(self, battleField):

        low_hero_list: List[Hero] = [msg_对己方兵力最低目标生效(self.target, battleField)]
        low_hero = 从队列确定受击单位(heroList=low_hero_list, skill=self.skill, hero=self.target, battleField=battleField, needRemove=True)

        Log().battle_L1('[{}]执行来自【{}】的[青囊急救]效果'.format(
            low_hero.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        # 驱散3种负面状态
        负面soul列表 = msg_负面状态列表(low_hero)
        驱散数量 = min(3, len(负面soul列表))
        while 驱散数量 > 0 and 负面soul列表:
            # 随机选择一个负面状态进行驱散
            要驱散的负面soul = random.choice(负面soul列表)
            要驱散的负面soul.restore_initial()
            负面soul列表.remove(要驱散的负面soul)
            驱散数量 -= 1

        # 恢复兵力
        治疗soul = Soul(
            target=low_hero,
            initiator=self.target,
            sourceType=SoulSourceType.武将战法,
            skill=self.skill,
            effect_type=SoulEffectType.恢复兵力,
            effect_value=治疗计算(battleField, 施救者=self.target, 受助者=low_hero, 治疗率 = self.skill.青囊急救_治疗系数())
        )
        治疗soul.deploy_initial()

class 青囊急救_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        soul = 青囊急救_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    def get_发动率(self):
        return 0.55

    def 青囊急救_治疗系数(self):
        return self.get_rank_bonus(2.6, 0.078)
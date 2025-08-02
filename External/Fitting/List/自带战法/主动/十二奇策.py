
# 战法名称: 十二奇策
# 战法类型: 主动
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.6

# 十二奇策:
# 对敌军随机两人造成220%谋略伤害,并施加随机1种异常状态(优先施加未持有的状态),持续两回合

# 异常状态:特殊负面状态
# 包括:震慑、缴械、技穷、混乱、嘲讽、虚弱、断粮、洪水、火攻、风暴、畏惧、妖术,共计12种

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, WeaponType, SkillFeature, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 十二奇策_info(BaseSkillInfo):
    def __init__(self):
        # 使用模板系统获取配置
        template = get_skill_template('主动_谋略', Fitting_List_Enum.十二奇策)
        super().__init__(template)

class 十二奇策_soul(BaseSkillSoul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.主动战法行动时 and hero == self.target:

            if not msg_主动战法发起判断(self.target):
                Log().battle_L0('[{}]战法【{}】无法释放'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return

            十二奇策skill: 十二奇策_skill = self.skill
            实际发动率 = (1 + self.target.get_主动战法发动率降低()) * 十二奇策skill.十二奇策_发动率()

            # 判断是否发动
            if random.random() > 实际发动率:
                Log().battle_L2('[{}]因几率未发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return
            Log().battle_L2('[{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

            attacked_heroes = 对敌方所有目标生效(self.target, battleField)
            attacked_times = min(2, len(attacked_heroes))
            for _ in range(attacked_times):

                if len(attacked_heroes) == 0:
                    break

                attacked: Hero = 从队列确定受击单位(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)

                damageModel = 计算伤害(battleField, self.target, attacked, SoulDamageType.谋略, SkillType.指挥, 伤害值= 2.2)
                damage_soul = Soul(target=attacked,
                                    initiator=self.target,
                                    sourceType=SoulSourceType.武将战法,
                                    skill= self.skill,
                                    effect_type=SoulEffectType.损失兵力,
                                    effect_value=damageModel.damage_value,
                                    source_soul=self,
                                    battleField=battleField,
                                    damage=damageModel)
                damage_soul.deploy_initial()

                real_abnormal = 生效未施加的异常状态(attacked, battleField)
                if real_abnormal == SoulEffectType.震慑:
                    from External.Fitting.List.Abnormal.震慑 import 震慑_soul
                    异常soul = 震慑_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.缴械:
                    from External.Fitting.List.Abnormal.缴械 import 缴械_soul
                    异常soul = 缴械_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.技穷:
                    from External.Fitting.List.Abnormal.技穷 import 技穷_soul
                    异常soul = 技穷_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.混乱:
                    from External.Fitting.List.Abnormal.混乱 import 混乱_soul
                    异常soul = 混乱_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.嘲讽:
                    from External.Fitting.List.Abnormal.嘲讽 import 嘲讽_soul
                    异常soul = 嘲讽_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.虚弱:
                    from External.Fitting.List.Abnormal.虚弱 import 虚弱_soul
                    异常soul = 虚弱_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.断粮:
                    from External.Fitting.List.Abnormal.断粮 import 断粮_soul
                    异常soul = 断粮_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.洪水:
                    from External.Fitting.List.Abnormal.洪水 import 洪水_soul
                    异常soul = 洪水_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.火攻:
                    from External.Fitting.List.Abnormal.火攻 import 火攻_soul
                    异常soul = 火攻_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.风暴:
                    from External.Fitting.List.Abnormal.风暴 import 风暴_soul
                    异常soul = 风暴_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.畏惧:
                    from External.Fitting.List.Abnormal.畏惧 import 畏惧_soul
                    异常soul = 畏惧_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                elif real_abnormal == SoulEffectType.妖术:
                    from External.Fitting.List.Abnormal.妖术 import 妖术_soul
                    异常soul = 妖术_soul(
                        target=attacked,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.战斗中,
                        duration=2,
                        source_soul=self,
                        battleField=battleField)
                
                if 异常soul.initiator.get_被击溃状态() != True and 异常soul.target.get_被击溃状态() != True:
                    Log().battle_L2('[{}]执行来自【{}】的[十二奇策-负面]效果'.format(attacked.get_武将名称().value, self.skill.get_战法名称().value))

                异常soul.deploy_initial()
                self.soul持有列表.append(异常soul)
                attacked.get_响应Soul列表().append(异常soul)

class 十二奇策_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        十二奇策soul = 十二奇策_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            skill=self)
        self.get_Soul_list().append(十二奇策soul)
        self.get_持有者().get_持有Soul列表().append(十二奇策soul)
        self.get_持有者().get_响应Soul列表().append(十二奇策soul)

    def 十二奇策_发动率(self):
        # 初始值为 0.6
        # 每一级升阶提升基础初始值为 0.01

        rankUp = self.get_战法升阶()
        value = 0.6 + rankUp * 0.01
        return value

    def 十二奇策_伤害系数(self):
        # 初始值为 220%
        # 每一级升阶提升基础初始值为 2.4%

        rankUp = self.get_战法升阶()
        value = 2.2 + rankUp * 0.024
        return value
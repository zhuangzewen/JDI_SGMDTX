# 战法名称: 携民渡江
# 战法类型: 指挥
# 战法特性: 治疗
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 携民渡江:
# 战斗开始时，提升我军全体18点统率(受智力影响), 
# 每回合结束时，恢复我军全体兵力(治疗率100%),然后驱散我军兵力最低单体1种负面状态并对其额外进行1次恢复(治疗率90%)

# 满阶携民渡江:
# 战斗开始时，提升我军全体20.5点统率(受智力影响), 
# 每回合结束时，恢复我军全体兵力(治疗率116%),然后驱散我军兵力最低单体1种负面状态并对其额外进行1次恢复(治疗率104%)

from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType,
    Fitting_List_Enum, Log, random, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 携民渡江_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('指挥_治疗', Fitting_List_Enum.携民渡江, 1.0)
        super().__init__(template)

class 携民渡江_soul(BaseSkillSoul):

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            self._deploy_统率效果(battleField)

        elif status == SoulResponseTime.回合结束时:
            self._deploy_治疗效果(battleField)

    def _deploy_统率效果(self, battleField):

        Log().battle_L1('[{}]发动战法【{}】'.format(
            self.target.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)
        value_times = len(value_heroes)
        
        for _ in range(value_times):
            if len(value_heroes) == 0:
                break

            目标武将 = 从队列确定受击单位(value_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            统率soul = self.skill.create_soul(
                target=目标武将,
                effectType=SoulEffectType.统率,
                effectValue=self.skill.携民渡江_统率提升系数(),
                damage=Damage(skillEffectName='携民渡江')
            )

            统率soul.deploy_initial()
            self.soul持有列表.append(统率soul)

    def _deploy_治疗效果(self, battleField):

        Log().battle_L1('[{}]执行来自【{}】的[携民渡江]效果'.format(
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
                effectType=SoulEffectType.恢复兵力,
                effectValue=治疗计算(battleField, 施救者=self.target, 受助者=目标武将, 治疗率 = self.skill.携民渡江_群体治疗系数())
            )
            全体治疗soul.deploy_initial()   

        low_hero:Hero = msg_对己方兵力最低目标生效(self.target, battleField)

        负面soul = msg_负面状态列表(low_hero)
        if len(负面soul) != 0:
            随机负面soul: Soul = random.choice(负面soul)
            随机负面soul.restore_initial()

        单点治疗soul = self.skill.create_soul(
            target=low_hero,
            effectType=SoulEffectType.恢复兵力,
            effectValue=治疗计算(battleField, 施救者=self.target, 受助者=low_hero, 治疗率 = self.skill.携民渡江_单体治疗系数())
        )
        单点治疗soul.deploy_initial()   

class 携民渡江_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        soul = 携民渡江_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    def 携民渡江_统率提升系数(self):
        def 拟合过程数据统计():
            # 初始值为 18
            # 每一级升阶提升基础初始值为 0.5

            # 智力 342.83
            # 统率提升 33.37
            # 提升值为 33.37 - 18 = 15.37

            # 智力 258.62
            # 统率提升 27.33
            # 提升值为 27.33 - 18 = 9.33

            # 智力 270.12
            # 统率提升 28.17
            # 提升值为 28.17 - 18 = 10.17

            # 智力 294.69
            # 统率提升 29.95
            # 提升值为 29.95 - 18 = 11.95

            # 智力 306.72
            # 统率提升 30.82
            # 提升值为 30.82 - 18 = 12.82

            # x 为智力, y 为提升值 
            # y = 0.07175227071078484*x+-9.209931942314372
            pass

        from Generals.JDI_Hero import Hero
        original_value = self.get_rank_bonus(18, 0.5)
        owner: Hero = self.get_持有者()
        x = owner.get_智力()
        y = 0.07175227071078484 * x - 9.209931942314372 + original_value
        return y

    def 携民渡江_群体治疗系数(self):
        return self.get_rank_bonus(1, 0.032)

    def 携民渡江_单体治疗系数(self):
        return self.get_rank_bonus(0.9, 0.028)
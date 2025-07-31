# 战法名称: 九伐中原
# 战法类型: 指挥
# 战法特性: 文武
# 适应兵种: 盾,枪,骑,弓
# 发动率: 100%

# 技能描述:
# 每个回合结束时进行1-3次讨伐对敌军随机两人造成40%兵刃和谋略伤害
# 我军全体造成伤害后会使当前回合讨伐伤害系数提升5%，可提升9次
# 累积讨伐3次后使敌军兵力最低单体产生逃兵(受智力和武力影响)

# y = 2.63515 * x - 701.515

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, Hero, Skill
)
from Calcu.JDI_Calculate import *
from Soul.Enum.SoulEffectType_Enum import SoulEffectType

class 九伐中原_info(BaseSkillInfo):
    """
    九伐中原战法信息类
    继承自基础技能信息模板，用于定义战法基本属性
    """
    def __init__(self):
        # 使用文武模板初始化指挥战法
        template = get_skill_template('指挥_文武', Fitting_List_Enum.九伐中原)
        super().__init__(template)

class 九伐中原_soul(BaseSkillSoul):
    """
    九伐中原战法灵魂类
    处理战法的具体效果逻辑和战场响应
    """
    def __init__(self, target: Hero, initiator: Hero, skill: Skill):
        super().__init__(target, initiator, skill=skill)
        self.讨伐伤害系数提升次数 = 0
        self.当前讨伐次数 = 0
        self.当前回合是否发动过讨伐 = False

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        """
        战场响应方法，处理不同阶段的技能效果
        :param status: 当前战场阶段
        :param battleField: 战场实例
        :param hero: 相关武将
        :param sourceSoul: 触发源灵魂
        """
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            Log().battle_L1(f'[{self.target.get_武将名称().value}]发动战法【九伐中原】')
            Log().battle_L2(f'[{self.target.get_武将名称().value}]的[九伐中原]效果已施加')

        elif status == SoulResponseTime.回合重置阶段:
            self.讨伐伤害系数提升次数 = 0
            self.当前回合是否发动过讨伐 = False
            # self.当前讨伐次数 不重置

        elif status == SoulResponseTime.回合结束时:
            # 执行讨伐伤害逻辑
            self._execute_讨伐_sequence(battleField)

        elif status == SoulResponseTime.造成伤害时:
            if (self.当前回合是否发动过讨伐 == True):
                return
            
            if (msg_判断在一个队伍中(self.target, hero, battleField) == False):
                return

            self._increase_damage_multiplier(hero)

    def _execute_讨伐_sequence(self, battleField):
        self.当前回合是否发动过讨伐 = True
        随机一到三次_times = random.randint(1, 3)
        Log().battle_L1(f'[{self.target.get_武将名称().value}]执行来自【九伐中原】的[九伐中原]效果')

        for i in range(随机一到三次_times):
            self.当前讨伐次数 += 1
            Log().battle_L1(f'[{self.target.get_武将名称().value}]执行来自【九伐中原】的[九伐中原-讨伐]效果')
            self._deal_讨伐_damage(battleField)
            self._check_逃兵_condition(battleField)

    def _deal_讨伐_damage(self, battleField):
        """
        造成讨伐伤害
        :param battleField: 战场实例
        :param damage_multiplier: 伤害系数
        """
        # 获取敌军目标
        attacked_heroes = 对敌方所有目标生效(self.target, battleField)
        attack_times = min(len(attacked_heroes), 2)
        for i in range(attack_times):

            attacked: Hero = 从队列确定受击单位(attacked_heroes)
            兵刃damage_soul = self.skill.create_damage_soul(
                battleField = battleField, 
                initiator = self.target,
                target = attacked, 
                damage_type = SoulDamageType.兵刃, 
                skill_type = SkillType.指挥, 
                damage_multiplier = (self.skill.九伐中原_讨伐伤害系数() + self.讨伐伤害系数提升次数 * self.skill.九伐中原_叠加系数()), 
                source_soul = self,
                effect_name = "九伐中原-讨伐",
            )
            兵刃damage_soul.deploy_initial()

            谋略damage_soul = self.skill.create_damage_soul(
                battleField = battleField, 
                initiator = self.target,
                target = attacked, 
                damage_type = SoulDamageType.谋略, 
                skill_type = SkillType.指挥, 
                damage_multiplier = (self.skill.九伐中原_讨伐伤害系数() + self.讨伐伤害系数提升次数 * self.skill.九伐中原_叠加系数()), 
                source_soul = self,
                effect_name = "九伐中原-讨伐",
            )
            谋略damage_soul.deploy_initial()

    def _increase_damage_multiplier(self, hero):

        Log().battle_L1(f'[{hero.get_武将名称().value}]执行来自【九伐中原】的[九伐中原]效果')
        if self.讨伐伤害系数提升次数 >= 9:
            Log().battle_L2(f'[{hero.get_武将名称().value}]的【九伐中原伤害提升】保持不变0(9)')
        else:
            self.讨伐伤害系数提升次数 += 1
            Log().battle_L2(f'[{self.target.get_武将名称().value}]的【九伐中原伤害提升】提升1({self.讨伐伤害系数提升次数})')

    def _check_逃兵_condition(self, battleField):

        if self.当前讨伐次数 / 3 < 1:
            return
        
        self.当前讨伐次数 -= 3
        low_hero:Hero = msg_对敌方兵力最低目标生效(self.target, battleField)
        if low_hero == None:
            return
        Log().battle_L1(f'[{self.target.get_武将名称().value}]执行来自【九伐中原】的[九伐中原-逃兵]效果')
        damage_soul = self.skill.create_damage_soul(
            battleField = battleField, 
            initiator = self.target,
            target = low_hero, 
            damage_type = SoulDamageType.文武逃兵, 
            skill_type = SkillType.指挥, 
            damage_multiplier = 0,
            source_soul = self,
            effect_name = '九伐中原-逃兵'
        )
        damage_soul.deploy_initial()

class 九伐中原_skill(BaseSkill):
    """
    九伐中原技能类，处理技能初始化和系数计算
    """
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        """
        初始化灵魂并添加到持有者
        """
        持有者and响应者 = self.get_持有者()
        soul = 九伐中原_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    def 九伐中原_讨伐伤害系数(self):
        return self.get_rank_bonus(0.4, 0.016)

    def 九伐中原_叠加系数(self):
        return self.get_rank_bonus(0.05, 0.002)

    

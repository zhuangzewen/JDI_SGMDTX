# 战法名称: 鹰视狼顾
# 战法类型: 主动
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 鹰视狼顾:
# 进行布局,获得随机1种布阵状态(优先获得不同的状态),持续到战斗结束,50%概率(受智力影响)再布局1次。
# 并对敌军机两人造成50%谋略伤害,每多持有1种布局可提供的状态,谋略伤害系数提升20%,可提升8次
# 目标：敌军群体；兵种：盾弓枪骑；概率：100%

# 布局后可提供的增益状态：
# 布局一：清醒
# 布局二：1层抵御
# 布局三：谋略伤害提升8%
# 布局四：15%奇谋
# 布局五：攻心提升10%
# 布局六：统率提升20点
# 布局七：智力提升20点
# 布局八：看破提升20%
#（已持有清醒和抵御时视为持有布局一和二）


from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, WeaponType, SkillFeature, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 鹰视狼顾_info(BaseSkillInfo):
    def __init__(self):
        # 使用模板系统获取配置
        template = get_skill_template('主动_谋略', Fitting_List_Enum.鹰视狼顾)
        super().__init__(template)

class 鹰视狼顾_布阵soul(BaseSkillSoul):
    def __init__(self, target: Hero, initiator: Hero, skill=None):
        super().__init__(target, initiator, skill=skill)
        self.soul持有列表 = []
        self.布局状态 = None
        self.增益效果 = []
        self.谋略伤害提升次数 = 0

class 鹰视狼顾_soul(BaseSkillSoul):
    def __init__(self, target: Hero, initiator: Hero, skill=None):
        super().__init__(target, initiator, skill=skill)
        self.soul持有列表 = []
        self.布局状态 = None
        self.增益效果 = []
        self.谋略伤害提升次数 = 0

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
       
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.主动战法行动时 and hero == self.target:
            
            if not msg_主动战法发起判断(self.target):
                Log().battle_L0('[{}]战法【{}】无法释放'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return
            
            # 实际发动率 = (1 + self.target.get_主动战法发动率降低()) * 1

            # # 判断是否发动
            # if random.random() > 实际发动率:
            #     Log().battle_L2('[{}]因几率未发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
            #     return
            Log().battle_L2('[{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))


    def _get_random_layout(self):
        # 随机获得一种布局状态
        layouts = ["清理布局", "层抵御布局", "谋略伤害提升布局", "攻击提升布局", "统率提升布局", "智力提升布局", "先攻提升布局"]
        return random.choice(layouts)

    def _get_layout_buff(self, layout):
        # 根据布局状态返回增益效果
        buffs = {
            "清理布局": "清理效果+1",
            "层抵御布局": "抵御层数+3",
            "谋略伤害提升布局": "谋略伤害+8%",
            "攻击提升布局": "攻击+10%",
            "统率提升布局": "统率+20",
            "智力提升布局": "智力+20",
            "先攻提升布局": "先攻+20"
        }
        return buffs.get(layout, "无")
    
class 鹰视狼顾_skill(BaseSkill):

    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        鹰视狼顾soul = 鹰视狼顾_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            skill=self)
        self.get_Soul_list().append(鹰视狼顾soul)
        self.get_持有者().get_持有Soul列表().append(鹰视狼顾soul)
        self.get_持有者().get_响应Soul列表().append(鹰视狼顾soul)

    def 鹰视狼顾_再次布阵概率(self, hero=None):
        # 计算再次布阵的概率，受智力影响
        # 套用韬光养晦的计算公式
        # y = 0.0001972619047618951*x+0.005635839285716829
        智力 = hero.get_当前智力()
        提高发动率 = 0.0001972619047618951 * 智力 + 0.005635839285716829
        return self.get_rank_bonus(0.5, 0.015) + 提高发动率
    
    def 鹰视狼顾_谋略伤害初始系数(self):
        return self.get_rank_bonus(0.5, 0.015)
    
    def 鹰视狼顾_每层布局提供伤害系数(self):
        return self.get_rank_bonus(0.2, 0.006)

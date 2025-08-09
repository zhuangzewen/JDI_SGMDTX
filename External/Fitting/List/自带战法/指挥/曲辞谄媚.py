from Soul.JDI_Soul import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, WeaponType, SkillFeature, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 曲辞谄媚_info(BaseSkillInfo):
    def __init__(self):
        # 使用模板系统获取配置
        template = get_skill_template('指挥_谋略', Fitting_List_Enum.曲辞谄媚)
        super().__init__(template)

class 曲辞谄媚_soul(BaseSkillSoul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill=skill)
        self.混乱概率 = 0.05
        self.回合计数 = 0

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.回合开始前:
            # 获取智力最高的队友
            智力最高队友 = max(
                [h for h in battleField.get_我方武将列表() if h != self.target],
                key=lambda h: h.get_智力(),
                default=None
            )
            
            if 智力最高队友:
                # 造成伤害提升效果
                伤害提升 = random.uniform(0.1, 0.3)
                伤害提升soul = Soul(
                    target=智力最高队友,
                    initiator=self.target,
                    sourceType=SoulSourceType.武将战法,
                    skill=self.skill,
                    effect_type=SoulEffectType.造成伤害提升,
                    effect_value=伤害提升,
                    duration=1,
                    source_soul=self,
                    battleField=battleField
                )
                伤害提升soul.deploy_initial()
                
                # 混乱效果
                if random.random() < self.混乱概率:
                    from External.Fitting.List.Abnormal.混乱 import 混乱_soul
                    混乱soul = 混乱_soul(
                        target=智力最高队友,
                        initiator=self.target,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        response_time=SoulResponseTime.内置待响应,
                        duration=1,
                        effect_type=SoulEffectType.混乱,
                        effect_value=0,
                        source_soul=self,
                        battleField=battleField
                    )
                    混乱soul.deploy_initial()
                
                self.混乱概率 += 0.05
                self.回合计数 += 1
        
        if status == SoulResponseTime.回合结束时:
            # 获取智力最高的队友
            智力最高队友 = max(
                [h for h in battleField.get_我方武将列表() if h != self.target],
                key=lambda h: h.get_智力(),
                default=None
            )
            
            if 智力最高队友:
                # 对敌方随机单体造成谋略伤害
                敌方武将列表 = battleField.get_敌方武将列表()
                if 敌方武将列表:
                    目标 = random.choice(敌方武将列表)
                    伤害系数 = random.uniform(0.5, 1.0)
                    
                    damageModel = 计算伤害(
                        battleField, 
                        智力最高队友, 
                        目标, 
                        SoulDamageType.谋略, 
                        SkillType.指挥, 
                        伤害值=伤害系数
                    )
                    
                    damage_soul = Soul(
                        target=目标,
                        initiator=智力最高队友,
                        sourceType=SoulSourceType.武将战法,
                        skill=self.skill,
                        effect_type=SoulEffectType.损失兵力,
                        effect_value=damageModel.damage_value,
                        source_soul=self,
                        battleField=battleField,
                        damage=damageModel
                    )
                    damage_soul.deploy_initial()

class 曲辞谄媚_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        曲辞谄媚soul = 曲辞谄媚_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            skill=self)
        self.get_Soul_list().append(曲辞谄媚soul)
        self.get_持有者().get_持有Soul列表().append(曲辞谄媚soul)
        self.get_持有者().get_响应Soul列表().append(曲辞谄媚soul)

# 战法名称: 见机行事
# 战法类型: 主动
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.4

# 见机行事:
# 提升我军智力最高单体智力10→20，我军武力最高单体武力10→20，持续2回合

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, Fitting_List_Enum, Log
)

class 见机行事_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('主动_辅助', Fitting_List_Enum.见机行事)
        super().__init__(template)
        self.战法描述 = "提升我军智力最高单体智力10→20，我军武力最高单体武力10→20，持续2回合"

class 见机行事_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.回合行动时:
            Log().battle_L1('[{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))
            
            # 提升智力效果
            int_soul = self.skill.create_soul(
                self.target, 
                SoulEffectType.智力提升, 
                self.skill.见机行事_智力提升()
            )
            int_soul.deploy_initial()
            
            # 提升武力效果
            str_soul = self.skill.create_soul(
                self.target, 
                SoulEffectType.武力提升, 
                self.skill.见机行事_武力提升()
            )
            str_soul.deploy_initial()

class 见机行事_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        soul = 见机行事_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )

        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    def 见机行事_智力提升(self):
        return self.get_rank_bonus(10, 1)

    def 见机行事_武力提升(self):
        return self.get_rank_bonus(10, 1)
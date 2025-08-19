
# 负面状态:
# 异常状态:
# 非控制状态:
# 妖术: 会心和奇谋伤害降低15%

from Soul.JDI_Soul import Soul
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Generals.JDI_Hero import Hero

class 妖术_soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 initiaTeam=None,
                 sourceType=None, 
                 sourceDetail=[SoulSourceDetail.负面状态效果, SoulSourceDetail.异常状态效果],
                 skill=None, 
                 responseTime=None, 
                 duration=-1, 
                 effectType=SoulEffectType.妖术, 
                 effectValue=0,
                 sourceSoul=None,
                 battleField=None):
         super().__init__(target, initiator, initiaTeam, sourceType, sourceDetail, skill, responseTime, duration, effectType, effectValue, sourceSoul, battleField)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将回合重置阶段 and hero == self.target:
            hero: Hero = self.target
            self.duration -= 1
            if self.duration < 0:
                self.restore_initial()
            return
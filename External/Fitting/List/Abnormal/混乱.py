
# 负面状态:
# 异常状态:
# 控制状态:
# 混乱: 普通攻击、追击战法和主动战法无差别选择目标

from Soul.JDI_Soul import Soul
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Generals.JDI_Hero import Hero

class 混乱_soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 initiaTeam=None,
                 sourceType=None, 
                 sourceDetail=[SoulSourceDetail.负面状态效果, SoulSourceDetail.异常状态效果, SoulSourceDetail.控制状态效果],
                 skill=None, 
                 response_time=None, 
                 duration=-1, 
                 effect_type=SoulEffectType.混乱, 
                 effect_value=0,
                 source_soul=None,
                 battleField=None):
         super().__init__(target, initiator, initiaTeam, sourceType, sourceDetail, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将回合重置阶段 and hero == self.target:
            hero: Hero = self.target
            self.duration -= 1
            if self.duration < 0:
                self.restore_initial()
            return
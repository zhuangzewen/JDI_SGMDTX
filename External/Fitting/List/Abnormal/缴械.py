
# 负面状态:
# 异常状态:
# 控制状态:
# 缴械: 无法普通攻击

from Soul.JDI_Soul import Soul
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Generals.JDI_Hero import Hero

class 缴械_soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 sourceType=None, 
                 sourceDetail=[SoulSourceDetail.负面状态效果, SoulSourceDetail.异常状态效果, SoulSourceDetail.控制状态效果],
                 skill=None, 
                 response_time=None, 
                 duration=-1, 
                 effect_type=SoulEffectType.缴械, 
                 effect_value=0,
                 source_soul=None,
                 battleField=None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将回合重置阶段 and hero == self.target:
            hero: Hero = self.target
            self.duration -= 1
            if self.duration < 0:
                self.restore_initial()
            return
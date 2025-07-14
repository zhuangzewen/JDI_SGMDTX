
# 负面状态:
# 异常状态:
# 控制状态:
# 技穷: 无法发动主动战法

from Soul.JDI_Soul import Soul
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Generals.JDI_Hero import Hero

class 技穷_soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 sourceType=None, 
                 skill=None, 
                 response_time=None, 
                 duration=-1, 
                 effect_type=None, 
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
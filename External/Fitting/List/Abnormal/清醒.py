
# 功能增益状态:
# 清醒: 使受到的控制状态(断粮、技穷、缴械、嘲讽、混乱、震慑、虚弱)暂时失去作用

from Soul.JDI_Soul import Soul
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Generals.JDI_Hero import Hero

class 清醒_soul(Soul):
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
         super().__init__(target, initiator, sourceType, sourceDetail, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将回合重置阶段 and hero == self.target:
            hero: Hero = self.target
            self.duration -= 1
            if self.duration < 0:
                self.restore_initial()
            return
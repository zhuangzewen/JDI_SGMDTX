
from Soul.JDI_Soul import Soul

class 震慑_soul(Soul):
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

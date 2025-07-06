
import random
from JDI_Log import Log

def 获取对比行动优先级(hero1_xg, hero2_xg):

    diff = abs(hero1_xg - hero2_xg)
    if diff < 30:
        p1 = 1.2 * diff + 50
    elif diff < 70:
        p1 = 0.35 * diff + 75.5
    else:
        p1 = 100

    randomValue = random.random()
    if randomValue * 100 < p1:
        return True if hero1_xg >= hero2_xg else False
    else:
        return False if hero2_xg >= hero1_xg else True
    
def int_随机一到两个敌方():
    return random.randint(1, 2)

def 根据受击率列表随机一个敌方(hit_rate_list):
    total_hit_rate = sum(hit_rate_list)
    # Log total_hit_rate
    Log().show_debug_info('DEBUG------- 受击率总和: {}'.format(total_hit_rate))
    if total_hit_rate == 0:
        return None
    random_value = random.uniform(0, total_hit_rate)
    Log().show_debug_info('DEBUG------- 随机受击率: {}'.format(random_value))
    cumulative_sum = 0.0
    for i, hit_rate in enumerate(hit_rate_list):
        cumulative_sum += hit_rate
        if cumulative_sum >= random_value:
            Log().show_debug_info('DEBUG------- 随机受击武将索引: {}'.format(i))
            return i
    return None

def 随机暴击伤害(攻击者, 伤害类型) -> float:
    from JDI_Log import Log
    from JDI_Hero import Hero
    from JDI_Enum import DamageType

    攻击者: Hero = 攻击者
    random_value = random.random()
    Log().show_debug_info('DEBUG------- 随机暴击率: {}'.format(random_value))
    if 伤害类型 == DamageType.谋略:
        if random_value <= 攻击者.get_奇谋几率():
            return 0.5
    elif 伤害类型 == DamageType.兵刃:
        if random_value <= 攻击者.get_会心几率():
            return 0.5
    return 0
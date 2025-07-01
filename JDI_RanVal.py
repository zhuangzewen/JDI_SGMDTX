
import random

def 获取对比行动优先级(hero1_xg, hero2_xg):
    # PDS同学的公式

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
    if total_hit_rate == 0:
        return None
    random_value = random.uniform(0, total_hit_rate)
    cumulative_sum = 0.0
    for i, hit_rate in enumerate(hit_rate_list):
        cumulative_sum += hit_rate
        if cumulative_sum >= random_value:
            return i
    return None
    
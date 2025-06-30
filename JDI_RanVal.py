
import random

def 获取对比行动优先级(hero1_xg, hero2_xg):
    diff = abs(hero1_xg - hero2_xg)
    p1 = 0.004 * diff ** 2 + 0.4343 * diff + 50
    randomValue = random.random()
    if randomValue * 100 < p1:
        return True if hero1_xg >= hero2_xg else False
    else:
        return False if hero2_xg >= hero1_xg else True
    

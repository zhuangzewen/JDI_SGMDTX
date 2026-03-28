import json
import random

class Hero:
    def __init__(self, name, hp=10000):
        self.name = name
        self.hp = hp  # 兵力
        self.max_hp = hp
    
    @property
    def alive(self):
        """血量大于0则存活"""
        return self.hp > 0

def load_heroes_from_json():
    """从 JSON 文件中加载武将信息"""
    with open('core/info/heroinfo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    heroes = []
    for hero_data in data['heroes']:
        hero = Hero(hero_data['name'])
        # 可以在这里添加更多属性
        heroes.append(hero)
    
    return heroes

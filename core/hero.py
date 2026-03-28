import json
import random

class Hero:
    def __init__(self, name, hp=10000, wuli=0, zhili=0, tongshuai=0, xiangong=0):
        self.name = name
        self.hp = hp  # 兵力
        self.max_hp = hp
        self.wuli = wuli  # 武力
        self.zhili = zhili  # 智力
        self.tongshuai = tongshuai  # 统帅
        self.xiangong = xiangong  # 先攻
    
    @property
    def alive(self):
        """血量大于 0 则存活"""
        return self.hp > 0

def load_heroes_from_json():
    """从 JSON 文件中加载武将信息"""
    with open('core/info/heroinfo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    heroes = []
    for hero_data in data['heroes']:
        # 从 JSON 中读取属性，如果没有则使用默认值
        stats = hero_data.get('stats', {})
        wuli = stats.get('strength', 0)
        zhili = stats.get('intelligence', 0)
        tongshuai = stats.get('leadership', 0)
        xiangong = stats.get('initiative', 0)
        
        hero = Hero(
            hero_data['name'],
            wuli=wuli,
            zhili=zhili,
            tongshuai=tongshuai,
            xiangong=xiangong
        )
        heroes.append(hero)
    
    return heroes

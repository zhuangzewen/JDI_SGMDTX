import random
from .hero import Hero
from .algo.algo import merge_sort_two_teams

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.attack_order = []  # 攻击顺序列表
    
    def add_random_heroes(self, hero_pool, count=3):
        """从武将池中随机添加指定数量的武将，不重复"""
        selected = random.sample(hero_pool, min(count, len(hero_pool)))
        for hero in selected:
            self.heroes.append(hero)
    
    def set_attack_order(self):
        """设置攻击顺序（按照武将列表顺序）"""
        self.attack_order = [hero for hero in self.heroes if hero.alive]
        return self.attack_order
    
    def recalculate_attack_order(self):
        """重新计算攻击顺序（按照先攻属性概率排序）"""
        alive_heroes = [hero for hero in self.heroes if hero.alive]
        # 使用概率算法排序
        self.attack_order = sort_by_initiative_probabilistic(alive_heroes)
        return self.attack_order
    
    def get_attack_order(self):
        """获取当前攻击顺序"""
        return self.attack_order
    
    def is_alive(self):
        """检查队伍是否还有存活的武将"""
        return any(hero.alive for hero in self.heroes)
    
    def get_alive_heroes(self):
        """获取所有存活的武将"""
        return [hero for hero in self.heroes if hero.alive]
    
    def attack(self, enemy_team):
        """我方所有存活武将按照攻击顺序攻击敌方队伍"""
        if not self.attack_order:
            self.set_attack_order()
        
        results = []
        
        for attacker in self.attack_order:
            # 检查攻击者是否存活
            if not attacker.alive:
                continue
            
            # 获取敌方存活的武将
            enemy_heroes = enemy_team.get_alive_heroes()
            if not enemy_heroes:
                break
            
            # 随机选择一个敌方武将作为目标
            target = random.choice(enemy_heroes)
            
            # 造成随机伤害（100-500）
            damage = random.randint(100, 500)
            target.hp -= damage
            if target.hp <= 0:
                target.hp = 0
            
            # 添加标记
            attacker_tag = "[我方]" if self.name == "我方" else "[敌方]"
            results.append(f"{attacker_tag} {attacker.name} 对 {target.name} 造成 {damage} 点伤害，剩余兵力：{target.hp}")
        
        return results

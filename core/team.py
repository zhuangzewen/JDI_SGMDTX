import random
from .hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    def add_random_heroes(self, hero_pool, count=3):
        """从武将池中随机添加指定数量的武将，不重复"""
        selected = random.sample(hero_pool, min(count, len(hero_pool)))
        for hero in selected:
            self.heroes.append(hero)
    
    def is_alive(self):
        """检查队伍是否还有存活的武将"""
        return any(hero.alive for hero in self.heroes)
    
    def get_alive_heroes(self):
        """获取所有存活的武将"""
        return [hero for hero in self.heroes if hero.alive]
    
    def attack(self, enemy_team):
        """我方所有存活武将攻击敌方队伍"""
        alive_heroes = self.get_alive_heroes()
        if not alive_heroes:
            return []
        
        results = []
        
        for attacker in alive_heroes:
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
            results.append(f"{attacker_tag} {attacker.name} 对 {target.name} 造成 {damage} 点伤害，剩余兵力: {target.hp}")
        
        return results

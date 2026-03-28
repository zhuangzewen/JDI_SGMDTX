class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    def is_alive(self):
        """检查队伍是否还有存活的武将"""
        return any(hero.alive for hero in self.heroes)
    
    def get_alive_heroes(self):
        """获取所有存活的武将"""
        return [hero for hero in self.heroes if hero.alive]

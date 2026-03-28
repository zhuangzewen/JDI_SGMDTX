class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.formation = None  # 当前阵型
        self.positions = {}  # 武将位置映射 {position_num: hero}
    
    def set_formation(self, formation):
        """设置阵型"""
        self.formation = formation
    
    def get_formation_effect(self):
        """获取阵型效果"""
        if self.formation:
            return self.formation.effect
        return "无阵型效果"
    
    def set_position(self, position_num, hero):
        """设置武将位置"""
        self.positions[position_num] = hero
    
    def get_position_effect(self, position_num):
        """获取指定位置的加成效果"""
        if self.formation:
            return self.formation.get_position_effect(position_num)
        return "无位置效果"
    
    def get_position_role(self, position_num):
        """获取指定位置的角色（前排/中排/后排）"""
        if self.formation:
            return self.formation.get_position_role(position_num)
        return "未知"
    
    def is_alive(self):
        """检查队伍是否还有存活的武将"""
        return any(hero.alive for hero in self.heroes)
    
    def get_alive_heroes(self):
        """获取所有存活的武将"""
        return [hero for hero in self.heroes if hero.alive]

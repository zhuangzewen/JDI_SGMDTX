from .team import Team

class Battle:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.round = 0
        self.max_rounds = 8
    
    def start_battle(self):
        """开始战斗"""
        self.round = 0  # 重置回合数
        print("=== 战斗开始 ===")
        
        while self.team1.is_alive() and self.team2.is_alive() and self.round < self.max_rounds:
            self.round += 1
            print(f"\n--- 第 {self.round} 回合 ---")
            
            # 我方攻击
            results1 = self.team1.attack(self.team2)
            for result in results1:
                print(result)
            
            # 检查敌方是否全部溃败
            if not self.team2.is_alive():
                break
            
            # 敌方攻击
            results2 = self.team2.attack(self.team1)
            for result in results2:
                print(result)
        
        # 战斗结束
        print("\n=== 战斗结束 ===")
        if self.team1.is_alive() and not self.team2.is_alive():
            print(f"{self.team1.name} 获胜！")
            return 1
        elif self.team2.is_alive() and not self.team1.is_alive():
            print(f"{self.team2.name} 获胜！")
            return 2
        else:
            print("平局！")
            return 0
    
    def get_remaining_hp(self, team):
        """获取队伍剩余总血量"""
        return sum(hero.hp for hero in team.heroes)

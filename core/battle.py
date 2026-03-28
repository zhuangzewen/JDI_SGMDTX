from .team import Team
from .algo.algo import merge_sort_two_teams

class Battle:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.round = 0
        self.max_rounds = 8
    
    def formation_phase(self):
        """布阵阶段：确定双方武将的攻击顺序"""
        print("\n=== 布阵阶段 ===")
        
        # 获取两队所有武将（包括已溃败的）
        team1_heroes = self.team1.heroes
        team2_heroes = self.team2.heroes
        
        # 使用两队交叉排序算法生成融合的攻击顺序
        merged_order = merge_sort_two_teams(team1_heroes, team2_heroes)
        
        # 将合并后的顺序分别设置到两队
        self._apply_merged_order(team1_heroes, team2_heroes, merged_order)
        
        # 显示融合后的攻击顺序
        print("融合攻击顺序：")
        for i, hero in enumerate(merged_order, 1):
            team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
            status = "溃败" if not hero.alive else f"{hero.hp}"
            print(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
        
        print()
    
    def start_battle(self):
        """开始战斗"""
        # 布阵阶段
        self.formation_phase()
        
        self.round = 0  # 重置回合数
        print("=== 战斗开始 ===")
        
        while self.team1.is_alive() and self.team2.is_alive() and self.round < self.max_rounds:
            self.round += 1
            print(f"\n--- 第 {self.round} 回合 ---")
            
            # 从第二回合开始，重新计算攻击顺序（两队交叉排序）
            if self.round > 1:
                # 获取两队所有武将（包括已溃败的）
                team1_heroes = self.team1.heroes
                team2_heroes = self.team2.heroes
                
                # 使用两队交叉排序算法
                merged_order = merge_sort_two_teams(team1_heroes, team2_heroes)
                
                # 将合并后的顺序分别设置到两队
                self._apply_merged_order(team1_heroes, team2_heroes, merged_order)
            
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
    
    def _apply_merged_order(self, team1_heroes, team2_heroes, merged_order):
        """
        将合并后的攻击顺序应用到两个队伍
        
        方法：
        1. 从合并顺序中提取各队的武将顺序
        2. 更新各队的 attack_order
        """
        # 提取 team1 的武将顺序
        team1_order = [hero for hero in merged_order if hero in team1_heroes]
        # 提取 team2 的武将顺序
        team2_order = [hero for hero in merged_order if hero in team2_heroes]
        
        # 更新两队的攻击顺序
        self.team1.attack_order = team1_order
        self.team2.attack_order = team2_order
        
        # 战斗结束
        print("\n=== 战斗结束 ===")
        team1_alive = self.team1.is_alive()
        team2_alive = self.team2.is_alive()
        
        if team1_alive and not team2_alive:
            print(f"{self.team1.name} 获胜！")
            return 1
        elif team2_alive and not team1_alive:
            print(f"{self.team2.name} 获胜！")
            return 2
        else:
            # 双方都全灭或平局
            print("平局！")
            return 0
    
    def get_remaining_hp(self, team):
        """获取队伍剩余总血量"""
        return sum(hero.hp for hero in team.heroes)

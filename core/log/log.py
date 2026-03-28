import os
from datetime import datetime

class BattleLogger:
    def __init__(self):
        self.log_entries = []
        self.html_entries = []
    
    def log(self, message):
        """添加日志条目"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.log_entries.append(entry)
        self.html_entries.append(f"<p>{entry}</p>")
    
    def log_battle_start(self, battle_count):
        """记录战斗开始"""
        self.log(f"=== 第 {battle_count} 局 ===")
    
    def log_formation(self, merged_order, team1_heroes, team2_heroes):
        """记录布阵阶段"""
        self.log("\n=== 布阵阶段 ===")
        self.log("行动顺序判断完毕：")
        for i, hero in enumerate(merged_order, 1):
            team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
            status = "溃败" if not hero.alive else f"{hero.hp}"
            self.log(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
        self.log("")
    
    def log_formation_effects(self, team_name, formation_name, effects):
        """记录阵型效果"""
        self.log(f"[{team_name}] 队获得【阵型——{formation_name}】强化效果")
        for hero_name, effect in effects:
            self.log(f"  {hero_name}: {effect}")
    
    def log_round_start(self, round_num):
        """记录回合开始"""
        self.log(f"\n--- 第 {round_num} 回合 ---")
    
    def log_round_order(self, merged_order, team1_heroes, team2_heroes):
        """记录回合行动顺序"""
        self.log("\n行动顺序判断完毕：")
        for i, hero in enumerate(merged_order, 1):
            team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
            status = "溃败" if not hero.alive else f"{hero.hp}"
            self.log(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
        self.log("")
    
    def log_attack(self, attacker_name, target_name, damage, remaining_hp, attacker_team_tag):
        """记录攻击"""
        target_team_tag = "[我方]" if attacker_team_tag == "[敌方]" else "[敌方]"
        self.log(f"{attacker_team_tag} {attacker_name} 对 {target_team_tag} {target_name} 造成 {damage} 点伤害，剩余兵力：{remaining_hp}")
    
    def log_battle_end(self, result, team1_name="我方", team2_name="敌方"):
        """记录战斗结束"""
        self.log("\n=== 战斗结束 ===")
        if result == 1:
            self.log(f"{team1_name} 获胜！")
        elif result == 2:
            self.log(f"{team2_name} 获胜！")
        else:
            self.log("平局！")
    
    def log_tournament_end(self, winner, team1_hp, team2_hp):
        """记录对战结束"""
        self.log(f"\n=== 对战结束 ===")
        if winner == "我方":
            self.log(f"我方获胜！")
        elif winner == "敌方":
            self.log(f"敌方获胜！")
        else:
            self.log(f"平局！")
        self.log(f"我方剩余总血量: {team1_hp}")
        self.log(f"敌方剩余总血量: {team2_hp}")
    
    def log_next_battle(self, battle_count):
        """记录进入下一局"""
        self.log(f"\n进入第 {battle_count + 1} 局...")
    
    def log_hero_selection(self, team_name, heroes):
        """记录武将选择"""
        self.log(f"\n{team_name} 选择的武将：")
        for hero in heroes:
            self.log(f"  - {hero.name} (武力：{hero.wuli}, 智力：{hero.zhili}, 统帅：{hero.tongshuai}, 先攻：{hero.xiangong})")
    
    def log_hp_change(self, hero_name, old_hp, new_hp, team_tag):
        """记录血量变化"""
        change = new_hp - old_hp
        if change > 0:
            self.log(f"  {team_tag} {hero_name}: {old_hp} → {new_hp} (+{change})")
        else:
            self.log(f"  {team_tag} {hero_name}: {old_hp} → {new_hp} ({change})")
    
    def log_random_result(self, name, value, description):
        """记录随机数结果"""
        self.log(f"  {name} 的随机结果: {value} ({description})")
    
    def log_round_summary(self, round_num, team1_hp, team2_hp):
        """记录回合总结"""
        self.log(f"\n--- 第 {round_num} 回合总结 ---")
        self.log(f"  我方剩余总血量: {team1_hp}")
        self.log(f"  敌方剩余总血量: {team2_hp}")
    
    def get_log_text(self):
        """获取日志文本"""
        return "\n".join(self.log_entries)
    
    def get_html_content(self):
        """获取 HTML 内容"""
        html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>战斗日志</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
        }
        .battle-section {
            margin: 20px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 5px;
            border-left: 4px solid #4CAF50;
        }
        .battle-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #2196F3;
            margin-bottom: 10px;
        }
        .round {
            margin: 10px 0;
            padding: 10px;
            background-color: #fff;
            border-radius: 3px;
            border: 1px solid #ddd;
        }
        .round-title {
            font-weight: bold;
            color: #666;
            margin-bottom: 5px;
        }
        .attack {
            margin: 3px 0;
            padding: 5px;
            background-color: #f0f0f0;
            border-radius: 2px;
        }
        .attacker-我方 {
            color: #2196F3;
        }
        .attacker-敌方 {
            color: #f44336;
        }
        .formation {
            margin: 10px 0;
            padding: 10px;
            background-color: #e8f5e9;
            border-radius: 3px;
        }
        .formation-item {
            margin: 2px 0;
            padding: 3px 5px;
            background-color: white;
            border-radius: 2px;
            display: inline-block;
            margin-right: 10px;
        }
        .formation-item.我方 {
            color: #2196F3;
        }
        .formation-item.敌方 {
            color: #f44336;
        }
        .result {
            font-weight: bold;
            padding: 10px;
            border-radius: 3px;
            margin: 10px 0;
        }
        .result.win {
            background-color: #e8f5e9;
            color: #4CAF50;
        }
        .result.lose {
            background-color: #ffebee;
            color: #f44336;
        }
        .result.draw {
            background-color: #fff3e0;
            color: #ff9800;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚔️ 三国谋定天下 - 战斗日志</h1>
"""
        for entry in self.html_entries:
            # 处理不同的日志类型
            if "=== 第" in entry and "局" in entry:
                html += f'        <div class="battle-section">\n'
                html += f'            <div class="battle-title">{entry.strip()}</div>\n'
            elif "=== 布阵阶段 ===" in entry:
                html += f'            <div class="formation">\n'
                html += f'                <strong>布阵阶段：</strong>\n'
            elif "融合攻击顺序：" in entry:
                continue  # 跳过标题行
            elif entry.strip().startswith("  ") and ". [" in entry:
                # 提取武将信息
                import re
                match = re.match(r'\s*(\d+)\.\s*\[([^\]]+)\]\s+([^\s(]+)\s+\(先攻：(\d+),\s+兵力：([^\)]+)\)', entry.strip())
                if match:
                    num, team, name, initiative, hp = match.groups()
                    team_class = "我方" if team == "我方" else "敌方"
                    html += f'                    <span class="formation-item {team_class}">{num}. {team} {name} (先攻：{initiative}, 兵力：{hp})</span>\n'
            elif entry.strip() == "":
                continue
            elif "=== 战斗结束 ===" in entry:
                html += f'            </div>\n'
                html += f'            <div class="result draw">战斗结束</div>\n'
            elif "我方获胜" in entry:
                html += f'            <div class="result win">{entry.strip()}</div>\n'
            elif "敌方获胜" in entry:
                html += f'            <div class="result lose">{entry.strip()}</div>\n'
            elif "--- 第" in entry and "回合" in entry:
                html += f'            <div class="round">\n'
                html += f'                <div class="round-title">{entry.strip()}</div>\n'
            elif entry.strip().startswith("[我方]") or entry.strip().startswith("[敌方]"):
                team = "我方" if entry.strip().startswith("[我方]") else "敌方"
                html += f'                <div class="attack {team}">{entry.strip()}</div>\n'
            elif "进入第" in entry and "局" in entry:
                html += f'        </div>\n'
                html += f'{entry.strip()}\n'
                html += f'        <div class="battle-section">\n'
            elif "=== 对战结束 ===" in entry:
                html += f'        </div>\n'
                html += f'        <div class="result draw">{entry.strip()}</div>\n'
            elif "我方剩余总血量" in entry:
                html += f'        <p>{entry.strip()}</p>\n'
            elif "敌方剩余总血量" in entry:
                html += f'        <p>{entry.strip()}</p>\n'
            else:
                html += f'        <p>{entry.strip()}</p>\n'
        
        html += """    </div>
</body>
</html>"""
        return html
    
    def save_log(self, filename="battle_log.txt"):
        """保存日志到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.get_log_text())
    
    def save_html(self, filename="battle_log.html"):
        """保存 HTML 到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.get_html_content())
    
    def open_html(self):
        """在浏览器中打开 HTML"""
        import webbrowser
        import os
        html_path = os.path.abspath("battle_log.html")
        webbrowser.open(f"file://{html_path}")

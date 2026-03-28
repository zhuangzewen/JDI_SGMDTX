import json
import os

class Formation:
    """阵型类"""
    def __init__(self, name, effect, description="", positions=None):
        self.name = name
        self.effect = effect
        self.description = description
        self.positions = positions if positions else {}
    
    def get_position_effect(self, position_num):
        """获取指定位置的加成效果"""
        if position_num in self.positions:
            pos_info = self.positions[position_num]
            return f"{pos_info['role']} - {pos_info['effect']}"
        return "无位置效果"
    
    def get_position_role(self, position_num):
        """获取指定位置的角色（前排/中排/后排）"""
        if position_num in self.positions:
            return self.positions[position_num]['role']
        return "未知"
    
    def __str__(self):
        return f"{self.name} - {self.effect}"

def load_formations_from_json():
    """从 JSON 文件加载阵型数据"""
    formation_list = []
    json_path = os.path.join(os.path.dirname(__file__), 'info', 'formationinfo.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for formation_data in data['formations']:
                formation = Formation(
                    name=formation_data['name'],
                    effect=formation_data['effect'],
                    description=formation_data.get('description', ''),
                    positions=formation_data.get('positions', {})
                )
                formation_list.append(formation)
    except FileNotFoundError:
        print(f"警告：阵型文件未找到 {json_path}")
    except json.JSONDecodeError:
        print(f"警告：阵型文件格式错误 {json_path}")
    
    return formation_list

def get_formation_by_name(name):
    """根据名称获取阵型"""
    formations = load_formations_from_json()
    for formation in formations:
        if formation.name == name:
            return formation
    return None

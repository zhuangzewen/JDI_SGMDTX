# 战法快速生成器
# 用于快速创建新的战法文件

import os
from typing import List, Dict, Optional
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from Generals.Enum.Generals_Enum import WeaponType

class SkillGenerator:
    """战法生成器类"""
    
    def __init__(self, base_path: str = "/Users/lx/Documents/JDI_SGMDTX/External/Fitting/List"):
        self.base_path = base_path
        
    def generate_skill_file(self, 
                           skill_name: str,
                           skill_type: SkillType,
                           skill_feature: SkillFeature,
                           weapon_types: List[WeaponType],
                           trigger_rate: float,
                           description: str,
                           max_description: str = None,
                           effects: List[Dict] = None,
                           custom_logic: str = None):
        """
        生成战法文件
        
        Args:
            skill_name: 战法名称
            skill_type: 战法类型
            skill_feature: 战法特性
            weapon_types: 适应兵种
            trigger_rate: 发动率
            description: 战法描述
            max_description: 满阶描述
            effects: 效果列表 [{'type': SoulEffectType, 'base': float, 'rank_bonus': float}]
            custom_logic: 自定义逻辑代码
        """
        
        # 确定文件路径
        type_folder = self._get_type_folder(skill_type)
        file_path = os.path.join(self.base_path, type_folder, f"{skill_name}.py")
        
        # 生成文件内容
        content = self._generate_file_content(
            skill_name, skill_type, skill_feature, weapon_types, 
            trigger_rate, description, max_description, effects, custom_logic
        )
        
        # 创建目录（如果不存在）
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ 战法文件已生成: {file_path}")
        return file_path
    
    def _get_type_folder(self, skill_type: SkillType) -> str:
        """根据战法类型获取文件夹路径"""
        type_mapping = {
            SkillType.被动: "自带战法/被动",
            SkillType.主动: "自带战法/主动", 
            SkillType.指挥: "自带战法/指挥",
            SkillType.追击: "自带战法/追击",
            SkillType.携带: "携带战法"
        }
        return type_mapping.get(skill_type, "其他")
    
    def _generate_file_content(self, skill_name, skill_type, skill_feature, 
                              weapon_types, trigger_rate, description, 
                              max_description, effects, custom_logic):
        """生成文件内容"""
        
        # 文件头部
        weapon_str = ",".join([wt.value for wt in weapon_types])
        header = f"""# 战法名称: {skill_name}
# 战法类型: {skill_type.value}
# 战法特性: {skill_feature.value}
# 适应兵种: {weapon_str}
# 发动率: {trigger_rate}

# {skill_name}:
# {description}
"""
        
        if max_description:
            header += f"""
# 满阶{skill_name}:
# {max_description}
"""

        # 导入部分
        imports = """
from External.Fitting.List.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, SKILL_TEMPLATES
)
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Control.Log.JDI_Log import Log
"""

        # Info类
        template_key = self._get_template_key(skill_type, skill_feature)
        info_class = f"""
class {skill_name}_info(BaseSkillInfo):
    def __init__(self):
        template = SKILL_TEMPLATES['{template_key}']
        template.skill_name = Fitting_List_Enum.{skill_name}
        super().__init__(template)
"""

        # Soul类
        soul_class = self._generate_soul_class(skill_name, effects, custom_logic)
        
        # Skill类
        skill_class = self._generate_skill_class(skill_name, effects)
        
        return header + imports + info_class + soul_class + skill_class
    
    def _get_template_key(self, skill_type: SkillType, skill_feature: SkillFeature) -> str:
        """获取模板键"""
        return f"{skill_type.value}_{skill_feature.value}"
    
    def _generate_soul_class(self, skill_name: str, effects: List[Dict], custom_logic: str) -> str:
        """生成Soul类"""
        if custom_logic:
            return custom_logic
            
        # 默认Soul类模板
        effects_code = ""
        if effects:
            effects_list = []
            for effect in effects:
                effects_list.append(f"(SoulEffectType.{effect['type']}, self.skill.{skill_name}_{effect['method']}())")
            
            effects_code = f"""
            # 创建多个效果
            effects = [
                {',\n                '.join(effects_list)}
            ]
            
            for effect_type, value in effects:
                soul = self.skill.create_soul(self.target, effect_type, value)
                soul.deploy_initial()
                self.soul持有列表.append(soul)"""
        
        return f"""
class {skill_name}_soul(BaseSkillSoul):
    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{{}}]发动战法【{{}}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            )){effects_code}
"""

    def _generate_skill_class(self, skill_name: str, effects: List[Dict]) -> str:
        """生成Skill类"""
        
        # 生成效果方法
        effect_methods = ""
        if effects:
            for effect in effects:
                method_name = f"{skill_name}_{effect['method']}"
                base_value = effect.get('base', 0)
                rank_bonus = effect.get('rank_bonus', 0)
                
                if rank_bonus != 0:
                    effect_methods += f"""
    def {method_name}(self):
        return self.get_rank_bonus({base_value}, {rank_bonus})
"""
                else:
                    effect_methods += f"""
    def {method_name}(self):
        return {base_value}
"""

        return f"""
class {skill_name}_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        soul = {skill_name}_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            sourceType=SoulSourceType.武将战法, 
            skill=self, 
            response_time=SoulResponseTime.内置待响应, 
            effect_type=SoulEffectType.无影响
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul){effect_methods}
"""

# 使用示例
def example_usage():
    generator = SkillGenerator()
    
    # 示例：创建一个新的被动战法
    generator.generate_skill_file(
        skill_name="钢筋铁骨",
        skill_type=SkillType.被动,
        skill_feature=SkillFeature.兵刃,
        weapon_types=[WeaponType.盾, WeaponType.枪],
        trigger_rate=1.0,
        description="战斗开始时，自身受到伤害降低20%，统帅提升15点",
        max_description="战斗开始时，自身受到伤害降低25%，统帅提升18点",
        effects=[
            {'type': '受到伤害', 'method': '受到伤害_降低系数', 'base': -0.2, 'rank_bonus': -0.01},
            {'type': '统帅', 'method': '统帅_提升系数', 'base': 15, 'rank_bonus': 0.6}
        ]
    )

if __name__ == "__main__":
    example_usage()

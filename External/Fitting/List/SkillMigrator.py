# 战法更新工具
# 用于将现有战法迁移到新的模板系统

import os
import re
from typing import List

class SkillMigrator:
    """战法迁移工具"""
    
    def __init__(self, base_path: str = "/Users/lx/Documents/JDI_SGMDTX/External/Fitting/List"):
        self.base_path = base_path
        
    def analyze_existing_skills(self) -> List[str]:
        """分析现有战法文件"""
        skills = []
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__') and file != 'SkillBaseTemplate.py':
                    skill_path = os.path.join(root, file)
                    skills.append(skill_path)
        return skills
    
    def get_migration_priority(self, skill_path: str) -> int:
        """获取迁移优先级 (数字越小优先级越高)"""
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 简单战法 - 只有基础属性修改
        if self._is_simple_skill(content):
            return 1
        # 中等复杂度 - 有一些自定义逻辑
        elif self._is_medium_skill(content):
            return 2  
        # 复杂战法 - 大量自定义逻辑
        else:
            return 3
    
    def _is_simple_skill(self, content: str) -> bool:
        """判断是否为简单战法"""
        # 检查是否只有基础的属性修改
        simple_patterns = [
            r'SoulEffectType\.(武力|智力|统帅|先攻)',
            r'SoulEffectType\.(造成伤害|受到伤害)',
            r'SoulEffectType\.连击几率'
        ]
        
        complex_patterns = [
            r'for.*in.*:',  # 循环
            r'if.*hero.*!=.*self',  # 复杂条件
            r'random\.',  # 随机逻辑
            r'calculate_.*\('  # 复杂计算
        ]
        
        has_simple = any(re.search(pattern, content) for pattern in simple_patterns)
        has_complex = any(re.search(pattern, content) for pattern in complex_patterns)
        
        return has_simple and not has_complex
    
    def _is_medium_skill(self, content: str) -> bool:
        """判断是否为中等复杂度战法"""
        return not self._is_simple_skill(content)
    
    def suggest_migration_order(self) -> List[tuple]:
        """建议迁移顺序"""
        skills = self.analyze_existing_skills()
        prioritized = []
        
        for skill_path in skills:
            priority = self.get_migration_priority(skill_path)
            skill_name = os.path.basename(skill_path).replace('.py', '')
            prioritized.append((priority, skill_name, skill_path))
        
        # 按优先级排序
        prioritized.sort(key=lambda x: x[0])
        return prioritized
    
    def generate_migration_report(self):
        """生成迁移报告"""
        migration_order = self.suggest_migration_order()
        
        print("🎯 战法迁移建议报告")
        print("=" * 50)
        
        priority_names = {1: "简单战法(优先迁移)", 2: "中等战法", 3: "复杂战法(最后迁移)"}
        
        current_priority = 0
        for priority, skill_name, skill_path in migration_order:
            if priority != current_priority:
                current_priority = priority
                print(f"\n📋 {priority_names[priority]}:")
                
            relative_path = skill_path.replace(self.base_path, "")
            print(f"   {priority}. {skill_name} ({relative_path})")
        
        return migration_order

# 运行分析
if __name__ == "__main__":
    migrator = SkillMigrator()
    migration_order = migrator.generate_migration_report()
    
    print(f"\n📊 统计信息:")
    priority_count = {1: 0, 2: 0, 3: 0}
    for priority, _, _ in migration_order:
        priority_count[priority] += 1
    
    print(f"   简单战法: {priority_count[1]} 个")
    print(f"   中等战法: {priority_count[2]} 个") 
    print(f"   复杂战法: {priority_count[3]} 个")
    print(f"   总计: {len(migration_order)} 个战法")

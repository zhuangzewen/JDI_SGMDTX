# -*- coding: utf-8 -*-
# 导入优化测试脚本
# 验证所有导入模块是否正常工作

import sys
import os

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

def test_import_module(module_name, description):
    """测试导入模块"""
    try:
        exec(f"from {module_name} import *")
        print(f"✅ {description} ({module_name}) - 导入成功")
        return True
    except Exception as e:
        print(f"❌ {description} ({module_name}) - 导入失败: {e}")
        return False

def test_specific_imports():
    """测试特定导入"""
    tests = [
        ("common_imports", "常用导入模块"),
        ("global_imports", "全局导入模块"),
        ("battlefield_imports", "战场系统导入"),
        ("hero_imports", "武将系统导入"),
        ("skill_imports", "技能系统导入"),
        ("soul_imports", "魂灵系统导入"),
    ]
    
    success_count = 0
    total_count = len(tests)
    
    print("🔍 开始测试导入模块...")
    print("=" * 50)
    
    for module, desc in tests:
        if test_import_module(module, desc):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 测试结果: {success_count}/{total_count} 个模块导入成功")
    
    if success_count == total_count:
        print("🎉 所有导入模块工作正常！")
    else:
        print("⚠️  部分导入模块存在问题，需要修复")
    
    return success_count == total_count

def test_battle_functionality():
    """测试战斗功能"""
    try:
        print("\n🎮 测试战斗功能...")
        import importlib
        
        # 动态导入模块
        common_module = importlib.import_module('Control.Imports.common_imports')
        
        # 测试关键组件
        get_hero_info = getattr(common_module, 'get_hero_info')
        Generals_Name_Enum = getattr(common_module, 'Generals_Name_Enum')
        TeamInfo = getattr(common_module, 'TeamInfo')
        Formation = getattr(common_module, 'Formation')
        
        # 创建简单的战斗测试
        team1_hero1 = get_hero_info(Generals_Name_Enum.诸葛亮)
        team1_hero1.set_extra(wl_extra=50, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
        
        team1 = TeamInfo(Formation.萁型阵, team1_hero1, team1_hero1, team1_hero1, '测试队伍')
        
        print("✅ 战斗功能组件创建成功")
        return True
        
    except Exception as e:
        print(f"❌ 战斗功能测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 JDI_SGMDTX 导入优化验证测试")
    print("=" * 60)
    
    # 测试导入模块
    imports_ok = test_specific_imports()
    
    # 测试战斗功能
    battle_ok = test_battle_functionality()
    
    print("\n" + "=" * 60)
    if imports_ok and battle_ok:
        print("🎊 所有测试通过！导入优化成功完成！")
        return 0
    else:
        print("💥 部分测试失败，需要进一步修复")
        return 1

if __name__ == "__main__":
    sys.exit(main())

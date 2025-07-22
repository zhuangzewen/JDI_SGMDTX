#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 测试迁移到 Control 系统后的武将文件导入

print("测试武将文件迁移...")

try:
    from Generals.List.诸葛亮 import 诸葛亮_info
    hero = 诸葛亮_info()
    print(f"✅ 诸葛亮导入成功 - 武将名称: {hero.武将名称}")
except Exception as e:
    print(f"❌ 诸葛亮导入失败: {e}")

try:
    from Generals.List.许褚 import 许褚_info
    hero = 许褚_info()
    print(f"✅ 许褚导入成功 - 武将名称: {hero.武将名称}")
except Exception as e:
    print(f"❌ 许褚导入失败: {e}")

try:
    from Generals.List.周瑜 import 周瑜_info
    hero = 周瑜_info()
    print(f"✅ 周瑜导入成功 - 武将名称: {hero.武将名称}")
except Exception as e:
    print(f"❌ 周瑜导入失败: {e}")

print("测试完成!")

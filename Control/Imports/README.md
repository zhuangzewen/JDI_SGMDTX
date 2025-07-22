# 导入模块文件夹 (Imports)

这个文件夹包含了所有用于简化导入的专用模块文件。通过使用这些模块，可以减少项目中重复的导入语句，提高代码的可维护性。

## 文件说明

### 📁 核心导入模块

- **`common_imports.py`** - 通用导入模块
  - 包含最常用的基础导入
  - 适用于一般文件使用
  - 使用方式: `from Control.Imports.common_imports import *`

- **`global_imports.py`** - 全局导入模块
  - 包含项目中所有可能需要的导入
  - 适用于需要完整功能的文件
  - 使用方式: `from Control.Imports.global_imports import *`

### 📁 专业系统导入模块

- **`battlefield_imports.py`** - 战场系统专用导入
  - 包含战场、战斗相关的所有导入
  - 适用于战斗系统开发
  - 使用方式: `from Control.Imports.battlefield_imports import *`

- **`hero_imports.py`** - 武将系统专用导入
  - 包含武将定义相关的导入
  - 适用于武将系统开发
  - 使用方式: `from Control.Imports.hero_imports import *`

- **`skill_imports.py`** - 技能系统专用导入
  - 包含技能、战法相关的导入
  - 适用于技能系统开发
  - 使用方式: `from Control.Imports.skill_imports import *`

- **`soul_imports.py`** - 魂灵系统专用导入
  - 包含魂灵效果相关的导入
  - 适用于魂灵系统开发
  - 使用方式: `from Control.Imports.soul_imports import *`

### 📁 测试工具

- **`test_imports.py`** - 导入测试工具
  - 用于验证所有导入模块是否正常工作
  - 包含自动化测试功能

## 使用指南

### 🎯 选择合适的导入模块

1. **一般文件** → 使用 `common_imports.py`
2. **战斗相关** → 使用 `battlefield_imports.py`
3. **武将定义** → 使用 `hero_imports.py`
4. **技能开发** → 使用 `skill_imports.py`
5. **魂灵效果** → 使用 `soul_imports.py`
6. **需要全部功能** → 使用 `global_imports.py`

### 💡 使用示例

```python
# 在主程序文件中
from Control.Imports.common_imports import *

# 在战斗系统文件中
from Control.Imports.battlefield_imports import *

# 在武将定义文件中
from Control.Imports.hero_imports import *
```

### ⚡ 优势

- **减少代码重复**: 导入语句从平均4-7行减少到1行
- **提高可维护性**: 集中管理导入，避免遗漏
- **增强代码整洁度**: 文件头部更加简洁
- **便于依赖管理**: 统一处理模块依赖关系

## 注意事项

- 所有导入模块都包含 `__all__` 定义，确保 `import *` 正常工作
- 如果需要添加新的导入，请在相应的模块文件中更新
- 测试新功能时，建议运行 `test_imports.py` 验证导入是否正常

## 更新历史

- **2025-07-22**: 创建导入模块文件夹，重构项目导入结构
- **优化效果**: 将导入代码量减少约75%，提高代码可维护性

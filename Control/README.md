# Control 控制系统文件夹

这个文件夹包含了项目的核心控制系统，负责管理项目的基础设施和支持功能。

## 文件夹结构

### 📁 Imports - 导入管理系统
位置: `Control/Imports/`

专门管理项目中所有的导入模块，提供便捷的导入方式：

- **`common_imports.py`** - 通用导入模块
- **`global_imports.py`** - 全局导入模块  
- **`battlefield_imports.py`** - 战场系统专用导入
- **`hero_imports.py`** - 武将系统专用导入
- **`skill_imports.py`** - 技能系统专用导入
- **`soul_imports.py`** - 魂灵系统专用导入
- **`test_imports.py`** - 导入测试工具
- **`README.md`** - 详细使用说明

### 📁 Log - 日志管理系统
位置: `Control/Log/`

负责项目的日志记录和管理：

- **`JDI_Log.py`** - 核心日志系统
- **`_Log/`** - 日志文件存储目录

## 使用指南

### 🎯 导入系统使用

```python
# 根据需要选择合适的导入模块
from Control.Imports.common_imports import *      # 一般用途
from Control.Imports.battlefield_imports import * # 战斗系统
from Control.Imports.hero_imports import *        # 武将系统
from Control.Imports.skill_imports import *       # 技能系统
from Control.Imports.soul_imports import *        # 魂灵系统
from Control.Imports.global_imports import *      # 完整功能
```

### 📝 日志系统使用

```python
from Control.Log.JDI_Log import Log

# 使用日志记录
Log.info("信息日志")
Log.error("错误日志")
Log.debug("调试日志")
```

## 优势

- **统一管理**: 所有控制相关功能集中在一个文件夹中
- **清晰结构**: 导入和日志系统分离，职责明确
- **便于维护**: 集中管理降低维护成本
- **模块化设计**: 每个子系统独立，易于扩展

## 更新历史

- **2025-07-22**: 创建 Control 文件夹，整合 Imports 和 Log 系统
- **架构改进**: 提升项目结构的组织性和可维护性

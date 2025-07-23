
# 准备创建一个 带创建时间的log文件 并防止中文乱码
import logging
import time
import os

# 如果 JDF_Log文件夹不存在，则创建一个JDF_Log文件夹
try:
    os.mkdir("Control/Log/_Log")
except FileExistsError:
    pass

logFileName = "Control/Log/_Log/JDI_Log_" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".log"
logging.basicConfig(filename=logFileName, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding="utf-8")

class Log():
    def __init__(self):
        self.show_all = True            # 全量信息  常态下为False
        self.show_system = True         # 系统信息  常态下为True
        self.show_battle = True         # 战斗信息  常态下为True   
        self.show_debug = True          # 调试信息  常态下为False
        
        # 缩进管理
        self._indent_level = 0
        self._indent_size = 4  # 每级缩进4个空格

    def _get_indent(self, level=None):
        """获取指定级别的缩进字符串"""
        if level is None:
            level = self._indent_level
        return ' ' * (level * self._indent_size)

    def _format_message(self, data, level=None):
        """格式化消息，添加缩进"""
        indent = self._get_indent(level)
        return f"{indent}{data}"

    def set_indent_level(self, level):
        """设置当前缩进级别"""
        self._indent_level = max(0, level)
        return self

    def increase_indent(self, amount=1):
        """增加缩进级别"""
        self._indent_level += amount
        return self

    def decrease_indent(self, amount=1):
        """减少缩进级别"""
        self._indent_level = max(0, self._indent_level - amount)
        return self

    def reset_indent(self):
        """重置缩进级别为0"""
        self._indent_level = 0
        return self

    # 原有方法保持兼容性
    def show_system_info(self, data='', level=None):
        formatted_data = self._format_message(data, level) if level is not None else data
        self.show_debug_info(formatted_data)
        if self.show_all == True or self.show_system == True:
            print(formatted_data)

    def show_battle_info(self, data='', level=None):
        formatted_data = self._format_message(data, level) if level is not None else data
        self.show_debug_info(formatted_data)
        if self.show_all == True or self.show_battle == True:
            print(formatted_data)

    def show_debug_info(self, data=''):
        if self.show_debug == True:
            logging.info(data)

    # 新增便捷方法
    def system_info(self, data='', indent=None):
        """系统信息 - 支持自动缩进"""
        if indent is not None:
            data = self._format_message(data, indent)
        self.show_system_info(data)

    def battle_info(self, data='', indent=None):
        """战斗信息 - 支持自动缩进"""
        if indent is not None:
            data = self._format_message(data, indent)
        self.show_battle_info(data)

    def debug_info(self, data='', indent=None):
        """调试信息 - 支持自动缩进"""
        if indent is not None:
            data = self._format_message(data, indent)
        self.show_debug_info(data)

    # 层级化便捷方法
    def system_L0(self, data=''):
        """顶级系统信息"""
        self.show_system_info(data, level=0)

    def system_L1(self, data=''):
        """一级系统信息"""
        self.show_system_info(data, level=1)

    def system_L2(self, data=''):
        """二级系统信息"""
        self.show_system_info(data, level=2)

    def battle_L0(self, data=''):
        """顶级战斗信息"""
        self.show_battle_info(data, level=0)

    def battle_L1(self, data=''):
        """一级战斗信息"""
        self.show_battle_info(data, level=1)

    def battle_L2(self, data=''):
        """二级战斗信息"""
        self.show_battle_info(data, level=2)

    def debug_L0(self, data=''):
        """顶级调试信息"""
        self.show_debug_info(self._format_message(data, level=0))

    def debug_L1(self, data=''):
        """一级调试信息"""
        self.show_debug_info(self._format_message(data, level=1))

    def debug_L2(self, data=''):
        """二级调试信息"""
        self.show_debug_info(self._format_message(data, level=2))

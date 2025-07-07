
# 准备创建一个 带创建时间的log文件 并防止中文乱码
import logging
import time
import os

# 如果 JDF_Log文件夹不存在，则创建一个JDF_Log文件夹
try:
    os.mkdir("_Log")
except FileExistsError:
    pass

logFileName = "_Log/JDI_Log_" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".log"
logging.basicConfig(filename=logFileName, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding="utf-8")

class Log():
    def __init__(self):
        self.show_all = True            # 全量信息  常态下为False
        self.show_system = True         # 系统信息  常态下为True
        self.show_battle = True         # 战斗信息  常态下为True   
        self.show_debug = True          # 调试信息  常态下为False

    def show_system_info(self, data = ''):
        self.show_debug_info(data)
        if self.show_all == True or self.show_system == True:
            print(data)

    def show_battle_info(self, data = ''):
        self.show_debug_info(data)
        if self.show_all == True or self.show_battle == True:
            print(data)

    def show_debug_info(self, data = ''):
        if self.show_debug == True:
            logging.info(data)

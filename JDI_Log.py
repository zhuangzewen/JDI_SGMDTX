
class Log():
    def __init__(self):
        self.show_all = True            # 全量信息  常态下为False
        self.show_system = True         # 系统信息  常态下为True
        self.show_battle = True         # 战斗信息  常态下为True    

    def show_system_info(self, data = ''):
        if self.show_all == True or self.show_system == True:
            print(data)

    def show_battle_info(self, data = ''):
        if self.show_all == True or self.show_battle == True:
            print(data)
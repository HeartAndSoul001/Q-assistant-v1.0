from PySide6.QtCore import QObject
from views import mainView
from controllers.ipHandle import ipHandleController
from controllers.configHandle import configHandleController

class mainController(QObject):
    """主页面控制器"""

    def __init__(self):
        super().__init__()
        self.view = mainView()
        # 连接导航栏信号
        self.view.nav_list.currentRowChanged.connect(self.view.set_current_page)

        # 创建各个模块的控制器
        self.ipHandle_controller = ipHandleController(self.view.ipHandle_view)
        self.configHandle_controller = configHandleController(self.view.configHandle_view)


    def show(self):
        """显示主页面"""
        self.view.show()

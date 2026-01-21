from PySide6.QtWidgets import (QWidget, QHBoxLayout, QStackedWidget, QListWidget, QListWidgetItem)
from PySide6.QtGui import (QGuiApplication, QPixmap, Qt)
from PySide6.QtCore import QSize
from views.ipHandle import ipHandleView
from views.configHandle import configHandleView
from views.ipAddressManage import ipAddressManageView
from utils import iconManager

class mainView(QWidget):
    """主页面视图"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 获取屏幕参数
        screen = QGuiApplication.primaryScreen().geometry()
        # 设置软件宽和高为屏幕参数的80%
        self.resize(int(screen.width()*0.6), int(screen.height()*0.6))
        # 移动软件居中
        self.move(int(screen.width()*0.2),int(screen.height()*0.2))
        # 设置软件标题和图标
        self.setWindowTitle('小Q助手')
        self.setWindowIcon(QPixmap("resources/images/Q.ico"))
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)


        # 主布局
        main_layout = QHBoxLayout(self)

        # 左侧导航栏
        self.nav_list = QListWidget(self)
        self.nav_list.setMinimumSize(QSize(80, 0))
        self.nav_list.setMaximumSize(QSize(130, 16777215))
        

        menu_list = ["IP地址管理","工具箱","配置处理"]
        
        for i in menu_list:
            a = QListWidgetItem(iconManager.get_icon(i),i,self.nav_list,0)
            a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.nav_list.addItem(a)
        
        main_layout.addWidget(self.nav_list,1)

        # 右侧功能显示区域
        self.stack = QStackedWidget(self)
        main_layout.addWidget(self.stack,4)

        # 初始化功能页面
        self.ipaddressManage_view = ipAddressManageView()
        self.ipHandle_view = ipHandleView()
        self.configHandle_view = configHandleView()


        # 添加功能页面到主视图
        self.add_page(self.ipaddressManage_view, 0)
        self.add_page(self.ipHandle_view, 1)
        self.add_page(self.configHandle_view, 2)




    def add_page(self, widget, index: int):
        """向右侧功能显示区域添加页面"""
        self.stack.insertWidget(index, widget)

    def set_current_page(self, index: int):
        """切换到指定页面"""
        self.stack.setCurrentIndex(index)
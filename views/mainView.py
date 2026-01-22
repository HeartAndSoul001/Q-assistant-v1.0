from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget, QListWidget, QListWidgetItem, QFrame, QPushButton)
from PySide6.QtGui import (QGuiApplication, QPixmap, Qt)
from PySide6.QtCore import QSize
from views.ipHandle import ipHandleView
from views.configHandle import configHandleView
from views.ipAddressManage import ipAddressManageView
from utils import iconManager

# 导航栏展开/收起时的宽度
NAV_EXPANDED_WIDTH = 152
NAV_COLLAPSED_WIDTH = 48


class mainView(QWidget):
    """主页面视图"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._nav_expanded = True
        self.init_ui()

    def init_ui(self):
        screen = QGuiApplication.primaryScreen().geometry()
        self.resize(int(screen.width() * 0.65), int(screen.height() * 0.7))
        self.move(int(screen.width() * 0.175), int(screen.height() * 0.15))
        self.setWindowTitle('小Q助手')
        self.setWindowIcon(QPixmap("resources/images/Q.ico"))
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 左侧导航栏容器（可收起）
        self.nav_container = QFrame(self)
        self.nav_container.setObjectName("mainNavContainer")
        self.nav_container.setFixedWidth(NAV_EXPANDED_WIDTH)
        nav_container_layout = QVBoxLayout(self.nav_container)
        nav_container_layout.setContentsMargins(0, 0, 0, 0)
        nav_container_layout.setSpacing(0)
        nav_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.nav_toggle_btn = QPushButton(self.nav_container)
        self.nav_toggle_btn.setObjectName("navToggleBtn")
        self.nav_toggle_btn.setFixedHeight(48)
        self._nav_icon_collapse = iconManager.get_icon("导航收起", colo="#d1d5db")
        self._nav_icon_expand = iconManager.get_icon("导航展开", colo="#d1d5db")
        self.nav_toggle_btn.setIcon(self._nav_icon_collapse)
        self.nav_toggle_btn.setToolTip("收起导航栏")
        self.nav_toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.nav_toggle_btn.clicked.connect(self._toggle_nav)
        self.nav_toggle_btn.setIconSize(QSize(20, 20))
        nav_container_layout.addWidget(self.nav_toggle_btn, 0, Qt.AlignmentFlag.AlignTop)

        self.nav_list = QListWidget(self.nav_container)
        self.nav_list.setObjectName("mainNav")
        self.nav_list.setSpacing(2)
        self.nav_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.nav_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        menu_list = ["IP地址管理", "工具箱", "配置处理"]
        for i in menu_list:
            a = QListWidgetItem(iconManager.get_icon(i), i, self.nav_list, 0)
            a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.nav_list.addItem(a)
        self.nav_list.setCurrentRow(0)
        nav_container_layout.addWidget(self.nav_list, 1)

        main_layout.addWidget(self.nav_container, 0)

        # 右侧功能显示区域（白底圆角容器）
        content_frame = QFrame(self)
        content_frame.setObjectName("contentStack")
        content_layout = QHBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget(content_frame)
        content_layout.addWidget(self.stack)
        main_layout.addWidget(content_frame, 1)

        # 初始化功能页面
        self.ipaddressManage_view = ipAddressManageView()
        self.ipHandle_view = ipHandleView()
        self.configHandle_view = configHandleView()


        # 添加功能页面到主视图
        self.add_page(self.ipaddressManage_view, 0)
        self.add_page(self.ipHandle_view, 1)
        self.add_page(self.configHandle_view, 2)




    def _toggle_nav(self):
        """切换导航栏收起/展开"""
        self._nav_expanded = not self._nav_expanded
        if self._nav_expanded:
            self.nav_container.setFixedWidth(NAV_EXPANDED_WIDTH)
            self.nav_list.setVisible(True)
            self.nav_toggle_btn.setIcon(self._nav_icon_collapse)
            self.nav_toggle_btn.setToolTip("收起导航栏")
        else:
            self.nav_container.setFixedWidth(NAV_COLLAPSED_WIDTH)
            self.nav_list.setVisible(False)
            self.nav_toggle_btn.setIcon(self._nav_icon_expand)
            self.nav_toggle_btn.setToolTip("展开导航栏")

    def add_page(self, widget, index: int):
        """向右侧功能显示区域添加页面"""
        self.stack.insertWidget(index, widget)

    def set_current_page(self, index: int):
        """切换到指定页面"""
        self.stack.setCurrentIndex(index)
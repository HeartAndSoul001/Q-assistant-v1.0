from PySide6.QtWidgets import QTabWidget
from .configGenView import configGenView
from .configExtraView import configExtraView
from utils import iconManager



class configHandleView(QTabWidget):
    """配置处理视图"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 创建二个选项卡
        ## 选项卡一:配置生成
        self.configGen_tab = configGenView("配置生成器")

        ## 选项卡二:配置提取
        self.configExtra_tab = configExtraView("配置提取器")


        # 将选项卡添加到QTabWidget
        self.addTab(self.configExtra_tab, iconManager.get_icon(self.configExtra_tab.name), self.configExtra_tab.name)
        self.addTab(self.configGen_tab, iconManager.get_icon(self.configGen_tab.name), self.configGen_tab.name)
        self.setTabToolTip(0,"配置提取器")
        self.setTabToolTip(1,"配置生成器")
        self.tabBar().setDocumentMode(True)
        self.tabBar().setExpanding(True)
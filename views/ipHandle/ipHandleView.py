from PySide6.QtWidgets import QTabWidget
from  .subnetsCalcuView import subnetsCalcuView
from  .ipformatTransView import ipformatTransView
from  .ipsetCalcuView import ipsetCalcuView
from utils import iconManager


class ipHandleView(QTabWidget):
    """IP 地址处理视图"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 创建三个选项卡
        # 选项卡一:IP子网掩码计算
        self.subnetsCalcu_tab = subnetsCalcuView("子网计算器")

        # # 选项卡二:IP格式转换
        self.ipFormatTrans_tab = ipformatTransView("格式转换")
        # # 选项卡三:IP集合运算
        self.ipSetCalcu_tab = ipsetCalcuView("集合运算")


        # 将选项卡添加到QTabWidget
        self.addTab(self.subnetsCalcu_tab, iconManager.get_icon(self.subnetsCalcu_tab.name), self.subnetsCalcu_tab.name)
        self.addTab(self.ipFormatTrans_tab, iconManager.get_icon(self.ipFormatTrans_tab.name), self.ipFormatTrans_tab.name)
        self.addTab(self.ipSetCalcu_tab, iconManager.get_icon(self.ipSetCalcu_tab.name), self.ipSetCalcu_tab.name)
        self.setTabToolTip(0,"IP子网计算器")
        self.setTabToolTip(1,"支持IP地址掩码与范围之间格式转换")
        self.setTabToolTip(2,"支持IP地址集合的合并、拆分等等")
        self.tabBar().setDocumentMode(True)
        self.tabBar().setExpanding(True)




from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox
from views.ipHandle import subnetsCalcuView
from models import subnetinfoModel
from netaddr import IPNetwork, AddrFormatError

class subnetsCalcuController(QObject):
    def __init__(self, view: subnetsCalcuView, model: subnetinfoModel):
        super().__init__()
        self.view = view
        self.model = model

        # 设置表格模型
        self.view.subnet_table_view.setModel(self.model)
        
        # 连接信号
        self._connect_signals()



    def _connect_signals(self):
        """连接信号槽"""
        self.view.ipv4_input_widget.inputCompleted.connect(self.init_table)
        self.view.subnet_table_view.doubleClicked.connect(self.view.copyContentToClipboard)
        self.view.subnet_table_view.entered.connect(self.view.showTooltip)

    @Slot(str)
    def init_table(self, ip: str):
        """处理IP地址输入并更新表格"""
        try:
            # 验证IP地址格式
            ip_network = IPNetwork(ip)
            
            # 更新表格数据
            self.model.showSubnetlist(str(ip_network))
            
            # 调整列宽
            self.view.subnet_table_view.resizeColumnsToContents()
            
        except AddrFormatError:
            QMessageBox.warning(
                self.view,
                "输入错误",
                "请输入有效的IP地址",
                QMessageBox.Ok
            )
        except Exception as e:
            QMessageBox.critical(
                self.view,
                "错误",
                f"发生错误: {str(e)}",
                QMessageBox.Ok
            )

    def clear_table(self):
        """清空表格数据"""
        self.model.beginResetModel()
        self.model.clear()
        self.model.endResetModel()


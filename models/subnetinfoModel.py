from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import Qt
from netaddr import (IPNetwork, IPAddress)  # 添加 IPAddress 导入

class subnetinfoModel(QStandardItemModel):
    HEADERS = ["子网前缀", "子网掩码", "反掩码", "地址范围", "子网号", "广播地址", "地址数量"]
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rows = 33
        self.columns = len(self.HEADERS)
        self.setRowCount(self.rows)
        self.setColumnCount(self.columns)
        
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if 0 <= section < len(self.HEADERS):
                return self.HEADERS[section]
        return super().headerData(section, orientation, role)
                

    def showSubnetlist(self, ip_str):
        try:
            ip = IPNetwork(ip_str)
            self.beginResetModel()
            
            for i in range(32, 0, -1):
                ip_network = IPNetwork(f"{ip.ip}/{i}")
                for col, value in enumerate([
                    str(i),
                    str(ip_network.netmask),
                    str(ip_network.hostmask),
                    f"{IPAddress(ip_network.first)}-{IPAddress(ip_network.last)}",  # 转换为点分十进制
                    str(ip_network.network),
                    str(ip_network.broadcast),
                    str(ip_network.size)
                ]):
                    self.setData(self.index(32-i, col), value, Qt.EditRole)
                    
                    self.item(32-i,col).setTextAlignment(Qt.AlignmentFlag.AlignCenter)


            self.endResetModel()
            
        except Exception as e:
            print(f"IP地址处理错误: {e}")

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from utils import iconManager




class wrongMessageBox(QMessageBox):
    def __init__(self, error_info, parent=None):
        super().__init__(parent)
        self.init_ui(error_info)

    def init_ui(self,error_info):
        self.setWindowFlags(Qt.WindowType.Window)
        self.setWindowIcon(iconManager.get_icon("警告提示",colo="red"))
        self.setWindowTitle("出错了！")
        self.setText(u"错误信息：\n{}".format(error_info))

class infoMessageBox(QMessageBox):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.init_ui(info)
    def init_ui(self, info):
        self.setWindowFlags(Qt.WindowType.Window)
        self.setWindowIcon(iconManager.get_icon("信息提示",colo="blue"))  # 更改图标为信息图标
        self.setWindowTitle("提示信息！")  # 更改标题
        self.setText(u"信息：\n{}".format(info))  # 更改文本
        self.setIcon(QMessageBox.Information)  # 设置为信息图标
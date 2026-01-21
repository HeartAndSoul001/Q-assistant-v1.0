from PySide6.QtWidgets import QTabWidget
from utils import iconManager



class ipAddressManageView(QTabWidget):
    """配置处理视图"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        pass
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QTableView, QHeaderView, QPushButton)
from views.components import (codeEditor, myComboBox, chooseWorkDir)


class configExtraView(QWidget):
    """配置提取视图"""

    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()
    
    def init_ui(self):
        pass
        


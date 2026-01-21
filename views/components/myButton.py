from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import (QIcon,QPixmap)

class myButton(QPushButton):
    def __init__(self, icon: QIcon | QPixmap, text: str, parent=None):
        super().__init__(icon,text,parent)
        self.init_ui()

    def init_ui(self):
        pass
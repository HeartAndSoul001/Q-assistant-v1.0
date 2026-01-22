from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
from PySide6.QtCore import Qt
from .codeEditor import codeEditor
from utils import iconManager




# 重写IP地址输入框（带两个功能按钮：1.从剪贴板粘贴 2.清除内容）
class inputBox(QWidget):
    def __init__(self, place_holder_text="", parent=None):
        super().__init__(parent)
        self.init_ui(place_holder_text)

    def init_ui(self, place_holder_text):
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        self.ipInput_tab = codeEditor(place_holder_text)
        self.ipInput_tab.setTabChangesFocus(True)

        self.ipInput_button_pastefromclipboard = QPushButton(iconManager.get_icon("从剪贴板粘贴"), "从剪贴板粘贴")
        self.ipInput_button_pastefromclipboard.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ipInput_button_pastefromclipboard.clicked.connect(lambda: self.pastefromclipboard(self.ipInput_tab))
        self.ipInput_button_clean = QPushButton(iconManager.get_icon("清除内容"), "清除内容")
        self.ipInput_button_clean.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ipInput_button_clean.clicked.connect(lambda: self.textClean(self.ipInput_tab))
        layout.addWidget(self.ipInput_tab, 0, 0, 4, 2)
        layout.addWidget(self.ipInput_button_pastefromclipboard, 5, 0, 1, 1)
        layout.addWidget(self.ipInput_button_clean, 5, 1, 1, 1)

    @property
    def inputText(self):
        return self.ipInput_tab.toPlainText()
    
    def clear_PlaceholderText(self):
        self.ipInput_tab.setPlaceholderText("")

    def pastefromclipboard(self, input_edit):
        self.clear_PlaceholderText()
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()
        if clipboard_text:
            input_edit.setPlainText(clipboard_text)

    def textClean(self,input_edit):
        input_edit.clear()
from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
from PySide6.QtGui import QClipboard
from PySide6.QtCore import Qt
from .codeEditor import codeEditor
from .myComboBox import myComboBox
from utils import iconManager



# 重写文本回显框（带两个功能按钮：1.复制到剪贴板 2.清除内容）
class outputBox(QWidget):
    def __init__(self, place_holder_text="", parent=None):
        super().__init__(parent)
        self.init_ui(place_holder_text)

    def init_ui(self,place_holder_text):
        layout = QGridLayout(self)
        layout.setSpacing(5)
        ## ip地址多行输入框
        self.ipOutput_tab = codeEditor(place_holder_text)
        self.ipOutput_tab.setReadOnly(True)


        ## ip地址输出框功能按钮1----复制到剪贴板
        self.ipOutput_button_copytoclipboard = QPushButton(iconManager.get_icon("复制内容到剪贴板"),"复制内容到剪贴板")
        self.ipOutput_button_copytoclipboard.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ipOutput_button_copytoclipboard.clicked.connect(self.copytoclipboard)
        ## ip地址输出框功能按钮2----清除内容
        self.ipOutput_button_clean = QPushButton(iconManager.get_icon("清除内容"),"清除内容")
        self.ipOutput_button_clean.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ipOutput_button_clean.clicked.connect(lambda: self.textClean(self.ipOutput_tab))
        ## ip地址输出框功能按钮3----选择分隔符
        self.ipOutput_button_split = myComboBox("分隔符:", ['\\n',',',';','space'])
        self.split_char = '\n'
        self.ipOutput_button_split.currentTextChanged.connect(self.split_change)

        layout.addWidget(self.ipOutput_tab,0,0,4,3)
        layout.addWidget(self.ipOutput_button_copytoclipboard,5,0,1,1)
        layout.addWidget(self.ipOutput_button_clean,5,1,1,1)
        layout.addWidget(self.ipOutput_button_split,5,2,1,1)



    def set_outputText(self,textStr):
        self.ipOutput_tab.setPlainText(textStr)

    def copytoclipboard(self):
        result_text = self.ipOutput_tab.toPlainText()
        # 获取粘贴板
        clipboard = QApplication.clipboard()

        # 将文本复制到粘贴板
        clipboard.setText(result_text, mode=QClipboard.Clipboard)
        clipboard.setText(result_text, mode=QClipboard.Selection)
    
    def textClean(self,input_edit):
        input_edit.clear()

    def split_change(self):
        if self.ipOutput_button_split.currentText() == '\\n':
            current_split_char = '\n'
        elif self.ipOutput_button_split.currentText() == 'space':
            current_split_char = ' '
        else:
            current_split_char = self.ipOutput_button_split.currentText()

        text = self.ipOutput_tab.toPlainText().replace(self.split_char, current_split_char)
        self.ipOutput_tab.setPlainText(text)
        self.split_char = current_split_char
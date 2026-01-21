from PySide6.QtWidgets import (QLabel, QWidget, QHBoxLayout, QHBoxLayout)
from PySide6.QtGui import (QRegularExpressionValidator)
from PySide6.QtCore import (Qt, QRegularExpression, QEvent, Signal)
from .myLineEdit import myLineEdit



class ipv4InputWidget(QWidget):
    # 定义ipv4地址的4个段
    ip = ["192","168","0","1"]
    # 定义ipv4地址某一段的校验正则
    ip_validator = QRegularExpressionValidator(QRegularExpression("(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})"))
    
    # 是否输入完成
    inputCompleted = Signal(str)


    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # 创建四个 QLineEdit 分别用于输入 IPv4 地址的四个段
        self.segment_inputs = [
            myLineEdit(self.ip_validator) for _ in range(4)]

        for index, input_field in enumerate(self.segment_inputs):
            input_field.setText(self.ip[index])  # 设置初始字段
            input_field.installEventFilter(self)
            input_field.pasteSignal.connect(self.pasteEvent)
        
            layout.addWidget(input_field)
            layout.setSpacing(5)

            if index < 3:
                # 在每两个输入框之间添加一个点，用 QLabel 实现
                dot_label = QLabel(".")
                dot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(dot_label)

        self.setLayout(layout)




    def eventFilter(self, obj, event):
        index = self.segment_inputs.index(obj)

        # 如果按下的键是点字符 '.', 移动焦点到下一个输入框
        if index < 3 and event.type() == QEvent.Type.KeyPress and event.text() == ".":
            self.segment_inputs[index + 1].setFocus()
            self.segment_inputs[index + 1].selectAll()
        
        if index > 0 and event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Backspace and len(obj.text()) == 0:
            self.segment_inputs[index - 1].setFocus()
            self.segment_inputs[index - 1].selectAll()

        # 如果按下的键是回车键，清除当前输入框的焦点
        if index == 3 and event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Return:
            self.segment_inputs[index].clearFocus()

        # 如果所有输入框都已经输入内容，检查是否全部失去焦点
        if all(input_field.text() for input_field in self.segment_inputs) and all(not input_field.hasFocus() for input_field in self.segment_inputs):
            ip_address = ".".join(input_field.text() for input_field in self.segment_inputs)
            self.inputCompleted.emit(ip_address)
        
        return super().eventFilter(obj, event)


    def pasteEvent(self,ipList):
        for i in range(len(ipList)):
            self.segment_inputs[i].setText(ipList[i])
            self.segment_inputs[i].clearFocus()
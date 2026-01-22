from PySide6.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton)
from views.components import (inputBox, outputBox)

class ipsetCalcuView(QWidget):
    """IP集合运算视图"""

    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IP集合运算")



        self.ipSetCalcu_content = QWidget()
        ipSetCalcu_content_layout = QGridLayout()
        ipSetCalcu_content_layout.setHorizontalSpacing(16)
        ipSetCalcu_content_layout.setVerticalSpacing(12)
        self.ipSetCalcu_content.setLayout(ipSetCalcu_content_layout)

        self.ipSetCalcu_inputbox1 = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        self.ipSetCalcu_inputbox2 = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        self.ipSetCalcu_outputbox = outputBox()
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_inputbox1, 0, 0, 1, 1)
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_inputbox2, 0, 1, 1, 1)
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_outputbox, 1, 0, 1, 2)

        self.ipSetCalcu_button_box = QWidget()
        ipSetCalcu_button_box_layout = QVBoxLayout()
        ipSetCalcu_button_box_layout.setSpacing(10)
        self.ipSetCalcu_button_box.setLayout(ipSetCalcu_button_box_layout)
        self.ipset_And_button = QPushButton("IP地址段--相交")
        self.ipset_Or_button = QPushButton("IP地址段--相加")
        self.ipset_Not_button = QPushButton("IP地址段--相减")
        ipSetCalcu_button_box_layout.addWidget(self.ipset_And_button)
        ipSetCalcu_button_box_layout.addWidget(self.ipset_Or_button)
        ipSetCalcu_button_box_layout.addWidget(self.ipset_Not_button)


        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(self.ipSetCalcu_content, 4)
        layout.addWidget(self.ipSetCalcu_button_box, 1)
        self.setLayout(layout)


    def setOutputBoxText(self, text):
        self.ipSetCalcu_outputbox.set_outputText(text)
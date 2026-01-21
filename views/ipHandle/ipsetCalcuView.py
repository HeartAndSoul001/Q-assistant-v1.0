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



        # IP地址内容框
        self.ipSetCalcu_content = QWidget()
        ipSetCalcu_content_layout = QGridLayout()
        self.ipSetCalcu_content.setLayout(ipSetCalcu_content_layout)

        ## IP输入框
        self.ipSetCalcu_inputbox1 = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        self.ipSetCalcu_inputbox2 = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        ## IP地址内容框
        self.ipSetCalcu_outputbox = outputBox()
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_inputbox1,0,0,1,1)
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_inputbox2,0,1,1,1)
        ipSetCalcu_content_layout.addWidget(self.ipSetCalcu_outputbox,1,0,1,2)

        # 功能按钮
        self.ipSetCalcu_button_box = QWidget()
        ipSetCalcu_button_box_layout = QVBoxLayout()
        self.ipSetCalcu_button_box.setLayout(ipSetCalcu_button_box_layout)
        ## 功能按钮1(IP地址集合--交集)
        self.ipset_And_button = QPushButton()
        self.ipset_And_button.setText("IP地址段--相交")
        ## 功能按钮2(IP地址集合--并集)
        self.ipset_Or_button = QPushButton()
        self.ipset_Or_button.setText("IP地址段--相加")
        ## 功能按钮3(IP地址集合--差集)
        self.ipset_Not_button = QPushButton()
        self.ipset_Not_button.setText("IP地址段--相减")
        ipSetCalcu_button_box_layout.addWidget(self.ipset_And_button)
        ipSetCalcu_button_box_layout.addWidget(self.ipset_Or_button)
        ipSetCalcu_button_box_layout.addWidget(self.ipset_Not_button)


        # 创建水平布局
        layout = QHBoxLayout()

        # 移除布局的边距
        layout.setContentsMargins(0, 0, 0, 0)  # 左、上、右、下边距设为0
        layout.setSpacing(0)  # 组件之间的间距设为0

        layout.addWidget(self.ipSetCalcu_content,4)
        layout.addWidget(self.ipSetCalcu_button_box,1)
        self.setLayout(layout)


    def setOutputBoxText(self, text):
        self.ipSetCalcu_outputbox.set_outputText(text)
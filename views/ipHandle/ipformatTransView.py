from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox)
from views.components import (inputBox, outputBox)

class ipformatTransView(QWidget):
    """IP格式转换视图"""

    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IP格式转换")

        # IP地址内容框
        self.ipFormatTrans_content = QWidget()
        ipFormatTrans_content_layout = QVBoxLayout()
        ## IP输入框
        self.ipFormatTrans_inputbox = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        ## 结果输出框
        self.ipFormatTrans_outputbox = outputBox()
        ipFormatTrans_content_layout.addWidget(self.ipFormatTrans_inputbox)
        ipFormatTrans_content_layout.addWidget(self.ipFormatTrans_outputbox)
        self.ipFormatTrans_content.setLayout(ipFormatTrans_content_layout)


        # 功能按钮
        self.ipFormatTrans_button_box = QWidget()
        ipFormatTrans_button_box_layout = QVBoxLayout()
        self.ipFormatTrans_button_box.setLayout(ipFormatTrans_button_box_layout)
        ## 功能按钮1(掩码形式)
        self.to_cidr_button = QPushButton()
        self.to_cidr_button.setText("掩码格式")
        ## 功能按钮2(地址范围形式)
        self.to_iprange_button = QPushButton()
        self.to_iprange_button.setText("地址范围格式")  
        ## 功能按钮3(地址清单形式)
        self.to_singleIP_button = QPushButton()
        self.to_singleIP_button.setText("地址清单形式")
        self.to_singleIP_button.setToolTip("显示输入地址段的所有单个IP清单")
        ipFormatTrans_button_box_layout.addWidget(self.to_cidr_button)
        ipFormatTrans_button_box_layout.addWidget(self.to_iprange_button)
        ipFormatTrans_button_box_layout.addWidget(self.to_singleIP_button)



        # 创建水平布局
        layout = QHBoxLayout()

        # 移除布局的边距
        layout.setContentsMargins(0, 0, 0, 0)  # 左、上、右、下边距设为0
        layout.setSpacing(0)  # 组件之间的间距设为0

        layout.addWidget(self.ipFormatTrans_content,4)
        layout.addWidget(self.ipFormatTrans_button_box,1)
        self.setLayout(layout)

    def setOutputBoxText(self, text):
        self.ipFormatTrans_outputbox.set_outputText(text)


    
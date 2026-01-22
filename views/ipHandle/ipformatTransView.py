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

        self.ipFormatTrans_content = QWidget()
        ipFormatTrans_content_layout = QVBoxLayout()
        ipFormatTrans_content_layout.setSpacing(12)
        self.ipFormatTrans_inputbox = inputBox("可接受输入IP格式：192.168.192.1,192.168.192.2/30,192.168.192.4-5,192.168.192.6-192.168.192.7")
        self.ipFormatTrans_outputbox = outputBox()
        ipFormatTrans_content_layout.addWidget(self.ipFormatTrans_inputbox)
        ipFormatTrans_content_layout.addWidget(self.ipFormatTrans_outputbox)
        self.ipFormatTrans_content.setLayout(ipFormatTrans_content_layout)

        self.ipFormatTrans_button_box = QWidget()
        ipFormatTrans_button_box_layout = QVBoxLayout()
        ipFormatTrans_button_box_layout.setSpacing(10)
        self.ipFormatTrans_button_box.setLayout(ipFormatTrans_button_box_layout)
        self.to_cidr_button = QPushButton("掩码格式")
        self.to_iprange_button = QPushButton("地址范围格式")
        self.to_singleIP_button = QPushButton("地址清单形式")
        self.to_singleIP_button.setToolTip("显示输入地址段的所有单个IP清单")
        ipFormatTrans_button_box_layout.addWidget(self.to_cidr_button)
        ipFormatTrans_button_box_layout.addWidget(self.to_iprange_button)
        ipFormatTrans_button_box_layout.addWidget(self.to_singleIP_button)



        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(self.ipFormatTrans_content, 4)
        layout.addWidget(self.ipFormatTrans_button_box, 1)
        self.setLayout(layout)

    def setOutputBoxText(self, text):
        self.ipFormatTrans_outputbox.set_outputText(text)


    
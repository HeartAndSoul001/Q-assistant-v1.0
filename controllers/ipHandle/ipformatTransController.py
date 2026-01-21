from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from views.ipHandle import ipformatTransView
from models import ipv4Model
from controllers.components import handleThread

class ipformatTransController(QObject):
    def __init__(self, view: ipformatTransView, model: ipv4Model):
        super().__init__()

        self.view = view
        self.model = model

        # 绑定视图与控制器
        self.view.to_cidr_button.clicked.connect(self.to_cidr_func)
        self.view.to_iprange_button.clicked.connect(self.to_iprange_func)  
        self.view.to_singleIP_button.clicked.connect(self.to_singleIP_func)


    def to_cidr_func(self):
        intextStr = self.view.ipFormatTrans_inputbox.inputText
        splitChar = self.view.ipFormatTrans_outputbox.split_char

        if intextStr == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.To_cidrStr, intextStr, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()

            
    
    def to_iprange_func(self):
        intextStr = self.view.ipFormatTrans_inputbox.inputText
        splitChar = self.view.ipFormatTrans_outputbox.split_char

        if intextStr == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.To_iprangeStr, intextStr, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()
  
    def to_singleIP_func(self):
        intextStr = self.view.ipFormatTrans_inputbox.inputText
        splitChar = self.view.ipFormatTrans_outputbox.split_char

        if intextStr == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.To_singleIPList, intextStr, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()
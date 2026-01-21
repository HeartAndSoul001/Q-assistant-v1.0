from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from views.ipHandle import ipsetCalcuView
from models import ipv4Model
from controllers.components import handleThread



class ipsetCalcuController(QObject):
    def __init__(self, view: ipsetCalcuView, model: ipv4Model):
        super().__init__()

        self.view = view
        self.model = model


        # 视图与控制器绑定
        self.view.ipset_And_button.clicked.connect(self.ipset_and_func)
        self.view.ipset_Or_button.clicked.connect(self.ipset_or_func)
        self.view.ipset_Not_button.clicked.connect(self.ipset_not_func)


    


    def ipset_and_func(self):
        intextStr1 = self.view.ipSetCalcu_inputbox1.inputText
        intextStr2 = self.view.ipSetCalcu_inputbox2.inputText
        splitChar = self.view.ipSetCalcu_outputbox.split_char

        if intextStr1 == "" or intextStr2 == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.ipsetStr_and, intextStr1, intextStr2, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()

    
    def ipset_or_func(self):
        intextStr1 = self.view.ipSetCalcu_inputbox1.inputText
        intextStr2 = self.view.ipSetCalcu_inputbox2.inputText
        splitChar = self.view.ipSetCalcu_outputbox.split_char

        if intextStr1 == "" or intextStr2 == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.ipsetStr_or, intextStr1, intextStr2, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()
        
    def ipset_not_func(self):
        intextStr1 = self.view.ipSetCalcu_inputbox1.inputText
        intextStr2 = self.view.ipSetCalcu_inputbox2.inputText
        splitChar = self.view.ipSetCalcu_outputbox.split_char

        if intextStr1 == "" or intextStr2 == "":
            self.view.setOutputBoxText("")
        else:
            work = handleThread(self.model.ipsetStr_not, intextStr1, intextStr2, splitChar)
            work.finished.connect(lambda: self.view.setOutputBoxText(work.result))
            work.error.connect(lambda error_msg: QMessageBox.critical(self.view, "IP地址输入错误", error_msg, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton))
            work.start()
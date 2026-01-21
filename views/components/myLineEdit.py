from PySide6.QtWidgets import (QLineEdit,QApplication)
from PySide6.QtCore import (Qt,Signal)
from PySide6.QtGui import (QKeyEvent)



# 输入框
## 输入校验、居中、点击选中所有文本
class myLineEdit(QLineEdit):

    # 是否存在粘贴行为
    pasteSignal = Signal(list)

    def __init__(self, ipseg_validator):
        super().__init__()
        self.ip_validator= ipseg_validator
        self.setValidator(self.ip_validator)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    

    # 单击选中所有
    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)
        self.selectAll()

    # 处理 Ctrl+V 粘贴行为
    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 检测 Ctrl+V 组合键
        if (event.modifiers() & Qt.ControlModifier) and event.key() == Qt.Key.Key_V:
            ipList = QApplication.clipboard().text().split(".")
            if len(ipList) != 4:
                return None
            # for i in ipList:
            #     if not re.match(self.ip_seg,i):
            #         return None
            self.pasteSignal.emit(ipList)
        else:
            super().keyPressEvent(event)
    
    # 处理右击粘贴行为
    def paste(self) -> None:
        ipList = QApplication.clipboard().text().split(".")
        if len(ipList) != 4:
            return None
        self.pasteSignal.emit(ipList)
        print(ipList)
        return super().paste()
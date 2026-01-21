from PySide6.QtWidgets import (QLineEdit, QFileDialog, QDialog, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox)
from PySide6.QtGui import (QMouseEvent, QIcon)
from PySide6.QtCore import (Qt, Signal, QFile)
from .clickableLabel import clickableLabel
import os



# 文件路径选择
class chooseWorkDir(QLineEdit):
    workDir = ""
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mousePressEvent(self, e: QMouseEvent) -> None:

        if e.button() == Qt.MouseButton.LeftButton:
            self.workDir = QFileDialog.getExistingDirectory(None, "请选择路径！", ".\\", QFileDialog.ShowDirsOnly)
            self.setText(self.workDir + "/")


class importDialog(QDialog):
    is_filePath_ready = Signal(str)

    def __init__(self, template_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("导入数据")
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon('./resources/images/Q.ico'))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.template_file = template_path

        # 创建组件
        self.file_import = clickableLabel("<p style=\"text-decoration: underline;\">请选择导入的文件！</p>", self)
        self.import_button = QPushButton("导入", self)
        self.cancel_button = QPushButton("取消", self)
        self.download_link = clickableLabel("<a href='./file/test.xlsx'>点击下载模板文件</a>",self)
        
        
        # 设置布局
        layout = QVBoxLayout()
        
        # 添加文件路径显示
        layout.addWidget(self.file_import, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 添加下载链接
        layout.addWidget(self.download_link, alignment=Qt.AlignmentFlag.AlignRight)
        
        # 创建按钮容器
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(button_container)
        
        # 设置主布局
        self.setLayout(layout)
        
        # 连接信号和槽
        self.file_import.clicked.connect(self.choose_file)
        self.download_link.clicked.connect(self.download_tempFile)
        self.import_button.clicked.connect(self.on_import_clicked)
        self.cancel_button.clicked.connect(self.close)

    def _init_clickedLabel(self):
        self.file_path = ""
        self.file_import.setText("<p style=\"text-decoration: underline;\">请选择导入的文件！</p>")
    
    def choose_file(self): 
        self.file_path, _ = QFileDialog.getOpenFileName(None,"选择文件","","Excel 文件 (*.xlsx)")
        if self.file_path != "":
            self.file_import.setText("<p style=\"text-decoration: underline;\">" + self.file_path + "</p>")
        
    def download_tempFile(self):
        template_file = QFile(self.template_file)
        save_path, _ = QFileDialog.getSaveFileName(None,"选择文件","import_tempFile.xlsx","Excel 文件 (*.xlsx)")
        if save_path:
            dst_file = QFile(save_path)
            if dst_file.exists():
                # 如果目标文件存在，先删除目标文件
                if not dst_file.remove():
                    print("Failed to remove existing destination file.")
                    return False            
            if template_file.copy(save_path):
                self.close()
            else:
                print("failed to copy file")
    

    def on_import_clicked(self):
        if self.file_path != "" and os.path.exists(self.file_path):
            self.is_filePath_ready.emit(self.file_path)
            self.close()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("提示")
            msg_box.setText("请先选择要导入的文件！")
            msg_box.setWindowIcon(QIcon('./resources/images/Q.ico'))
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec_()
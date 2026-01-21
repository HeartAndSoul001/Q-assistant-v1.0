from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QTableView, QHeaderView, QPushButton, QLineEdit)
from views.components import (codeEditor, myComboBox, chooseWorkDir,importDialog)




class configGenView(QWidget):
    """配置生成视图"""

    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()
    
    def init_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 左、上、右、下边距设为0
        layout.setSpacing(0)  # 组件之间的间距设为0
        self.setLayout(layout)

        # 常用模板填充
        


        # 添加模板文本填写区域
        # 对 "${}" 标注的变量进行提取并高亮显示
        self.template_area = codeEditor(placeholderStr="请用${***}代替变量编写脚本！\nrule ${index} permit ip source ${src_ip} destination ${dst_ip}", 
                                        syntax_high_lighter=[{"name":"","regularExpression":r"\$\{[\S ]*?\}","textCharFormat":""}])
        

        # 添加变量显示区域
        self.variable_area = QTableView(self)
        self.variable_area.resizeColumnsToContents()
        self.variable_area.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.variable_area.setAlternatingRowColors(True)
        
        self.variable_area.setMouseTracking(True)
        self.variable_area.setWordWrap(False)


        # 添加功能区域
        func_area = QWidget()
        func_area_layout = QHBoxLayout()
        # 移除布局的边距
        func_area_layout.setContentsMargins(0, 10, 0, 0)  # 左、上、右、下边距设为0
        func_area_layout.setSpacing(15)  # 组件之间的间距设为0
        func_area.setLayout(func_area_layout)
        ## 导入变量按钮
        self.import_button = QPushButton("变量导入")
        self.import_dialog = importDialog("./resources/file/import_template.xlsx")
        self.import_dialog.move(self.geometry().center() + self.import_dialog.geometry().center())

        ### 导出模式：单文件 Or 多文件
        self.export_mode = myComboBox(name="模式:",content=["单文件","多文件"])

        ### 导出目录路径
        self.export_dir = chooseWorkDir(self)
        self.export_dir.setPlaceholderText("选择导出路径")
        self.export_dir.setStyleSheet("border-radius:0px;")
        self.export_dir.setReadOnly(True)

        ### 导出文件名：
        #### 单文件：自输入字符串
        #### 多文件：变量名组合字符串
        self.export_name = QLineEdit()
        self.export_name.setPlaceholderText("请输入导出文件名，可以${param}调用导入的变量")
        self.export_name.setStyleSheet("border-radius:0px;")
        ### 导出按钮
        self.export_button = QPushButton("导出")


        func_area_layout.addWidget(self.import_button)
        func_area_layout.addWidget(self.export_mode)
        func_area_layout.addWidget(self.export_dir)
        func_area_layout.addWidget(self.export_name)
        func_area_layout.addWidget(self.export_button)


        layout.addWidget(self.template_area)
        layout.addWidget(self.variable_area)
        layout.addWidget(func_area)

    def show_fileImport_dialog(self):
        self.import_dialog._init_clickedLabel()
        self.import_dialog.show()

    
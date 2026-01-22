from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QTableView, QHeaderView, QPushButton, QLineEdit, QFileDialog, QAbstractItemView)
from views.components import (codeEditor, myComboBox, chooseWorkDir, importDialog)




class configGenView(QWidget):
    """配置生成视图"""

    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()
    
    def init_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        self.setLayout(layout)

        # 常用模板填充
        


        # 添加模板文本填写区域
        # 对 "${}" 标注的变量进行提取并高亮显示
        self.template_area = codeEditor(placeholderStr="请用${***}代替变量编写脚本！\nrule ${index} permit ip source ${src_ip} destination ${dst_ip}", 
                                        syntax_high_lighter=[{"name":"","regularExpression":r"\$\{[\S ]*?\}","textCharFormat":""}])
        

        # 添加变量显示区域
        self.variable_area = QTableView(self)
        self.variable_area.verticalHeader().setVisible(False)
        self.variable_area.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.variable_area.setAlternatingRowColors(True)
        self.variable_area.setMouseTracking(True)
        self.variable_area.setWordWrap(False)
        self.variable_area.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.variable_area.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


        # 添加功能区域
        func_area = QWidget()
        func_area_layout = QHBoxLayout()
        # 移除布局的边距
        func_area_layout.setContentsMargins(0, 8, 0, 0)
        func_area_layout.setSpacing(12)
        func_area.setLayout(func_area_layout)
        ## 导入变量按钮
        self.import_button = QPushButton("变量导入")
        self.import_dialog = importDialog("./resources/file/import_template.xlsx")
        self.import_dialog.move(self.geometry().center() + self.import_dialog.geometry().center())

        ### 导出模式：单文件 Or 多文件
        self.export_mode = myComboBox(name="模式:",content=["单文件","多文件"])

        ### 导出目录路径
        self.export_dir = chooseWorkDir(self)
        self.export_dir.setPlaceholderText("点击选择或使用右侧按钮")
        self.export_dir.setReadOnly(True)

        self.export_dir_btn = QPushButton("选择导出路径")
        self.export_dir_btn.setToolTip("选择配置导出目录")
        self.export_dir_btn.clicked.connect(self._choose_export_dir)

        self.export_name = QLineEdit()
        self.export_name.setPlaceholderText("请输入导出文件名，可${param}调用导入的变量")

        self.export_button = QPushButton("导出")
        self.export_button.setObjectName("primaryButton")

        func_area_layout.addWidget(self.import_button)
        func_area_layout.addWidget(self.export_mode)
        func_area_layout.addWidget(self.export_dir_btn)
        func_area_layout.addWidget(self.export_dir, 1)
        func_area_layout.addWidget(self.export_name, 1)
        func_area_layout.addWidget(self.export_button)


        layout.addWidget(self.template_area)
        layout.addWidget(self.variable_area)
        layout.addWidget(func_area)

    def _choose_export_dir(self):
        path = QFileDialog.getExistingDirectory(self, "选择导出路径", ".\\")
        if path:
            self.export_dir.setText(path + "/")

    def show_fileImport_dialog(self):
        self.import_dialog._init_clickedLabel()
        self.import_dialog.show()

    
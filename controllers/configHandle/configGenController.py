from PySide6.QtCore import QObject
from views.components import (infoMessageBox, wrongMessageBox)
from views.configHandle import configGenView
from models import variableModel
from utils import (is_valid_txtFilename)
from string import Template
import os
import re


class configGenController(QObject):
    def __init__(self, view:configGenView, model:variableModel):
        super().__init__()

        self.view = view
        self.model = model

        self.view.variable_area.setModel(model)



        # 连接信号
        self._connect_signals()


    def _connect_signals(self):
        self.view.import_button.clicked.connect(self.view.show_fileImport_dialog)
        self.view.import_dialog.is_filePath_ready.connect(self.model.load_data_from_xlsx)
        self.view.export_button.clicked.connect(self.export_file)


    def export_file(self):
        template_text = self.view.template_area.toPlainText()
        variable_area_column_count = self.view.variable_area.model().columnCount()
        variable_area_row_count = self.view.variable_area.model().rowCount()

        if template_text == "":
            wrong = wrongMessageBox("模板文本为空！")
            wrong.show()
            raise ValueError("模板文本为空！")
        
        if not os.path.exists(self.view.export_dir.text()):
            wrong = wrongMessageBox("导出路径不存在！")
            wrong.show()
            raise ValueError("导出路径不存在！")
        
        if self.view.export_name.text() == "":
            wrong = wrongMessageBox("导出文件名为空！")
            wrong.show()
            raise ValueError("导出文件名为空！")
        
        if self.model._data == []:
            wrong = wrongMessageBox("变量表为空！")
            wrong.show()
            raise ValueError("变量表为空！")

        # 创建一个模板
        template = Template(template_text)

        result = []
        # 遍历每一行
        for row in range(0,variable_area_row_count):
            # 遍历每一列
            paramm_dic = dict()
            for column in range(variable_area_column_count):
                paramm_dic[self.model._headers[column]] = self.model.get_data(row,column)
            result.append(template.substitute(paramm_dic))

        if self.view.export_mode.currentText() == "单文件":
            export_file_name = self.view.export_name.text() + ".txt"
            if is_valid_txtFilename(export_file_name):
                with open(self.view.export_dir.text() + export_file_name, "w", encoding="utf-8") as f:
                    f.write("\n".join(result))
                infoMessageBox("导出成功！").exec_()
            else:
                wrong = wrongMessageBox("导出文件名 {} 不合法！".format(export_file_name))
                wrong.show()
                raise ValueError("导出文件名 {} 不合法！".format(export_file_name))

        elif self.view.export_mode.currentText() == "多文件":
            params = re.findall(r"\$\{([\S ]+?)\}", self.view.export_name.text())
            if len(params) == 0:
                wrong = wrongMessageBox("文件名 {} 不存在变量，无法生成多文件！".format(self.view.export_name.text()))
                wrong.show()
                raise ValueError("文件名 {} 不存在变量，无法生成多文件！".format(self.view.export_name.text()))
            for param in params:
                if param not in self.model._headers:
                    wrong = wrongMessageBox("变量名 {} 不存在！".format(param))
                    wrong.show()
                    raise ValueError("变量名 {} 不存在！".format(param))
            
            # 创建一个模板
            file_name_template = Template(self.view.export_name.text())
            # 遍历每一行
            for row in range(1,variable_area_row_count):
            # 遍历每一列
                paramm_dic = dict()
                for column in range(variable_area_column_count):
                    paramm_dic[self.model._headers[column]] = self.model.get_data(row,column)
                file_name = file_name_template.substitute(paramm_dic) + ".txt"
                if is_valid_txtFilename(file_name):
                    with open(self.view.export_dir.text() + file_name, "w", encoding="utf-8") as f:
                        f.write(result[row-1])    
                else:
                    wrong = wrongMessageBox("导出文件名 {} 不合法！".format(file_name))
                    wrong.show()
                    raise ValueError("导出文件名 {} 不合法！".format(file_name))
            infoMessageBox("导出成功！").exec_()
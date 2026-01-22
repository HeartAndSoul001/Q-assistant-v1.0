from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableView, QHeaderView, QAbstractItemView, 
                               QApplication, QToolTip)
from PySide6.QtCore import (QMimeData,QModelIndex,Qt)
from PySide6.QtGui import (QCursor,QFontMetrics)
from views.components import ipv4InputWidget

class subnetsCalcuView(QWidget):
    def __init__(self, name = "", parent=None):
        super().__init__(parent)
        self.name = name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("子网掩码计算")

        self.ipv4_input_widget = ipv4InputWidget()
        self.subnet_table_view = QTableView()
        
        
        # 设置框架样式
        self.subnet_table_view.verticalHeader().setVisible(False)   # 隐藏垂直标题
        self.subnet_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.subnet_table_view.resizeColumnsToContents()
        self.subnet_table_view.setAlternatingRowColors(True)
        self.subnet_table_view.setMouseTracking(True)
        self.subnet_table_view.setWordWrap(False)
        self.subnet_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.subnet_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(self.ipv4_input_widget)
        layout.addWidget(self.subnet_table_view)
        
        # 设置布局
        self.setLayout(layout)



    # 捕捉双击事件，将内容复制到剪贴板
    def copyContentToClipboard(self, index:QModelIndex):
        # 捕捉双击事件，将内容复制到剪贴板
        if index is not None:
            clipboard = QApplication.clipboard()
            mime_data = QMimeData()
            mime_data.setText(index.data())
            clipboard.setMimeData(mime_data)
            
            # 显示气泡提示信息
            ## 获取全局鼠标位置
            global_pos = QCursor.pos()
            rect = self.subnet_table_view.visualRect(index)
            QToolTip.showText(global_pos, '已复制', self.subnet_table_view, rect, 5000)

    # 捕捉鼠标悬停事件，对于超宽内容显示气泡提示信息
    def showTooltip(self, item):
        columnWidth = self.subnet_table_view.columnWidth(item.column())
        text = self.subnet_table_view.model().data(item, Qt.DisplayRole)
        fontWidth = QFontMetrics(self.subnet_table_view.font()).horizontalAdvance(text)
        if columnWidth < fontWidth + 30:
            QToolTip.showText(QCursor.pos(), text, msecShowTime=-1)



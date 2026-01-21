from PySide6.QtWidgets import (QLabel, QHBoxLayout, QHBoxLayout, QComboBox, 
                               QSizePolicy, QFrame, QLayout)


class myComboBox(QFrame):
    def __init__(self, name="下拉框", content=[], parent=None):
        super().__init__(parent)
        self.label = name
        self.comboItems = content
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        # 名称
        self.box_label = QLabel(self.label)
        layout.addWidget(self.box_label)

        # 下拉菜单
        self.combo_box = QComboBox()
        self.combo_box.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        self.currentTextChanged = self.combo_box.currentTextChanged
        layout.addWidget(self.combo_box)
        self.combo_box.addItems(self.comboItems)
    

    def currentText(self):
        return self.combo_box.currentText()
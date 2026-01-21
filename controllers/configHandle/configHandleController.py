from PySide6.QtCore import QObject
from views.configHandle import configHandleView
from models import variableModel
from .configGenController import configGenController
from .configExtraController import configExtraController


class configHandleController(QObject):
    def __init__(self, view:configHandleView):
        super().__init__()

        self.view = view
        self.variable_model = variableModel()

        self.configGen_controller = configGenController(self.view.configGen_tab,self.variable_model)
        self.configExtra_controller = configExtraController(self.view.configExtra_tab,self.variable_model) 



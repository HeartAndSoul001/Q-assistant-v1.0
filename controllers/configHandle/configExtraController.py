from PySide6.QtCore import QObject
from views.configHandle import configExtraView
from models import variableModel



class configExtraController(QObject):
    def __init__(self, view:configExtraView, model:variableModel):
        super().__init__()

        self.view = view
        self.model = model
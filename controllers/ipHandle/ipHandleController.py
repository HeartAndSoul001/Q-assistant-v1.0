from PySide6.QtCore import QObject
from views.ipHandle import ipHandleView
from models import (subnetinfoModel, ipv4Model)
from .subnetsCalcuController import subnetsCalcuController
from .ipformatTransController import ipformatTransController
from .ipsetCalcuController import ipsetCalcuController


class ipHandleController(QObject):
    def __init__(self, view:ipHandleView):
        super().__init__()

        self.view = view

        self.subnetInfo_model = subnetinfoModel()
        self.ipv4_model = ipv4Model()

        self.subnetsCalcu_controller = subnetsCalcuController(view.subnetsCalcu_tab,self.subnetInfo_model)
        self.ipFormatTrans_controller = ipformatTransController(view.ipFormatTrans_tab,self.ipv4_model)
        self.ipSetCalcu_controller = ipsetCalcuController(view.ipSetCalcu_tab,self.ipv4_model)
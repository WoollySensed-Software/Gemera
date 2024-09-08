import pyqtgraph as pyg

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSize

from settings import CFG_PATH
from bin.handlers.types import *
from bin.handlers.ConfigurationFile import ConfigurationFileH


class GraphH(QWidget):

    def __init__(self, widget: QWidget):
        super().__init__()
        self.view = pyg.PlotWidget(widget)
        self.view.setMinimumSize(QSize(470, 470))
        self.view.showGrid(x=True, y=True)
    
    @staticmethod
    def setCfgOption(option: tuple) -> Nothing:
        key, val = option
        pyg.setConfigOption(key, val)

    def plotGraph(self, data: tuple[list, list]) -> Nothing:
        cfg_handler = ConfigurationFileH(CFG_PATH, use_exists_check=False)
        cfg_data = cfg_handler.get('graph')

        self.curve = self.view.plotItem.plot(name=cfg_data['name'], 
                                             pen=cfg_data['pen'])
        x, y = data
        self.curve.setData(x, y)

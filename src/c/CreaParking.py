from PyQt4 import QtGui
from src.v.Ui_CreaParking import Ui_CreaParking

__author__ = 'sidya'


class CreaParking:
    def __init__(self):
        self.w = QtGui.QWidget()
        self.ui = Ui_CreaParking()
        self.ui.setupUi(self.w)
        self.w.show()
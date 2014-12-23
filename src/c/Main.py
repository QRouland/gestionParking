import sys

from PyQt4 import QtGui

from src.v.MainWindow import Ui_MainWindow
from src.c.log.log import Log


__author__ = 'sidya'


class Main:
    def __init__(self):
        # Init des logs
        self.log = Log()

        #Liste Clients et Parking
        self.__clients = {}
        self.__Parkings = {}

        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.view)

        #Chargement activité
        self.loadLastActivity()
        self.ui.addListeParkings(10)

        self.view.show()
        sys.exit(app.exec_())


    def activity(self, msg, lvl):
        self.log.printL(msg, lvl)
        self.ui.addItemActivite(self.activite.readlines()[-1])

    def loadLastActivity(self):
        try:
            self.activite = open("log/activity.log", "r")
        except IOError:
            self.activite = open("log/activity.log", "w")
            self.activite.close()
            self.activite = open("log/activity.log", "r")

        liste = self.activite.readlines()
        for l in [l[:-1] for l in liste[-11:-1]]:
            self.ui.addItemActivite(l)

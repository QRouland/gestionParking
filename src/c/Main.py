import sys

from PyQt4 import QtGui

from src.v.MainWindow import Ui_MainWindow
from src.c.log.log import Log
from src.m.Parking import Parking, ListeTypePlace

__author__ = 'sidya'


class Main:
    def __init__(self):
        # Init des logs
        self.log = Log()

        l = ListeTypePlace()
        l.add(10, 11, 5)
        l.add(7, 12, 5)
        p = Parking(5, l,"lol")

        #Liste Clients et Parking
        self.__clients = []
        self.__parkings = [p]



        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.view)

        #Chargement activité
        self.loadLastActivity()
        self.majListeParking()

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

    def majListeParking(self):
        self.ui.majListeParkings(self.__parkings)

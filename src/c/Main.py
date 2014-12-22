from PyQt4 import QtGui
import sys
from src.v.MainWindow import Ui_MainWindow
from src.c.log.log import Log

__author__ = 'sidya'


class Main:
    def __init__(self):
        #Init des logs
        self.log = Log()

        app = QtGui.QApplication(sys.argv)
        self.view = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.view)

        #Chargement activité
        self.loadLastActivity()


        self.view.show()
        sys.exit(app.exec_())


    def activity(self,msg,lvl):
        self.log.printL(msg,10)
        self.ui.addItemActivite(self.activite.readlines()[-1])

    def loadLastActivity(self):
        try:
            self.activite = open("log/activity.log", "r")
        except IOError :
            self.activite = open("log/activity.log", "w")
            self.activite.close()
            self.activite = open("log/activity.log", "r")

        liste = self.activite.readlines()
        for l in [l[:-1] for l in liste[-11:-1]]:
            self.ui.addItemActivite(l)

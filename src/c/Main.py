import sys

from PyQt4 import QtGui

from src.c.CreaParking import CreaParking
from src.c.log.log import Log
from src.m.Parking import Parking, ListeTypePlace
from src.v.Ui_MainWindow import Ui_MainWindow

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

        #connect
        self.ui.comboBox.currentIndexChanged['QString'].connect(self.selectParking)
        self.ui.btn_creer.clicked.connect(self.creerParking)

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


    def addItemActivite(self, line):
        self.log.addItem(line)

    def majListeParking(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("Selectionner un parking")
        for p in self.__parkings:
            self.ui.comboBox.addItem(p.nom)

    def selectParking(self):
        self.ui.nom.clear()
        self.ui.niveau.clear()
        self.ui.placesParNiveau.clear()
        self.ui.placesDispo.clear()
        self.ui.placesSuperAbo.clear()
        if(self.ui.comboBox.currentIndex() != 0) :
            self.ui.nom.setText(self.__parkings[self.ui.comboBox.currentIndex()-1].nom)
            self.ui.niveau.setText(str(self.__parkings[self.ui.comboBox.currentIndex()-1].nbNiveau))
            self.ui.placesParNiveau.setText(str(self.__parkings[self.ui.comboBox.currentIndex()-1].nbPlacesParNiveau))
            self.ui.placesDispo.setText(str(self.__parkings[self.ui.comboBox.currentIndex()-1].nbPlacesLibresParking))
            self.ui.placesSuperAbo.setText("lol")


    def creerParking(self):
        self.view.hide()
        CreaParking()
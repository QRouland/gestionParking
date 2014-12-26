import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QTranslator, QLocale

from src.c.log.log import Log
from src.c.log.log import lvl

from src.c.CreaParking import CreaParking
from src.m.Parking import Parking, ListeTypePlace
from src.v.MyQMainWindow import MyQMainWindow
from src.v.Ui_MainWindow import Ui_MainWindow

__author__ = 'sidya'


class Main:
    def __init__(self):
        # Init des logs
        self.lvl = lvl()
        self.__log = Log()

        l = ListeTypePlace()
        l.add(10, 11, 5)
        l.add(7, 12, 5)
        p = Parking(5, l,"lol")

        #Liste Clients et Parking
        self.__clients = []
        self.__parkings = [p]



        app = QtGui.QApplication(sys.argv)


        self.__view = MyQMainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__view)

        #connect
        self.__ui.comboBox.currentIndexChanged['QString'].connect(self.selectParking)
        self.__ui.btn_creer.clicked.connect(self.creerParking)


        #Chargement activité
        self.loadLastActivity()

        self.showWindow()
        sys.exit(app.exec_())


    def activity(self, msg, lvl):
        self.__log.printL(msg, lvl)
        self.addItemActivite(self.activite.readlines()[-1])

    def loadLastActivity(self):
        try:
            self.activite = open("log/activity.log", "r")
        except IOError:
            self.activite = open("log/activity.log", "w")
            self.activite.close()
            self.activite = open("log/activity.log", "r")

        liste = self.activite.readlines()
        for l in [l[:-1] for l in liste[-11:-1]]:
            self.addItemActivite(l)


    def addItemActivite(self, line):
        self.__ui.listWidget.addItem(line)

    def majListeParking(self):
        self.__ui.comboBox.clear()
        self.__ui.comboBox.addItem("Selectionner un parking")
        for p in self.__parkings:
            self.__ui.comboBox.addItem(p.nom)

    def selectParking(self):
        self.__ui.nom.clear()
        self.__ui.niveau.clear()
        self.__ui.placesParNiveau.clear()
        self.__ui.placesDispo.clear()
        self.__ui.placesSuperAbo.clear()
        if(self.__ui.comboBox.currentIndex() != 0) :
            self.__ui.nom.setText(self.__parkings[self.__ui.comboBox.currentIndex()-1].nom)
            self.__ui.niveau.setText(str(self.__parkings[self.__ui.comboBox.currentIndex()-1].nbNiveau))
            self.__ui.placesParNiveau.setText(str(self.__parkings[self.__ui.comboBox.currentIndex()-1].nbPlacesParNiveau))
            self.__ui.placesDispo.setText(str(self.__parkings[self.__ui.comboBox.currentIndex()-1].nbPlacesLibresParking))
            self.__ui.placesSuperAbo.setText("lol")


    def creerParking(self):
        self.__view.hide()
        self.__widgetCourant = CreaParking(self)

    def addParking(self,parking):
        self.__parkings.append(parking)

    def showWindow(self):
        self.majListeParking()
        self.__view.show()
        self.__widgetCourant = None #supprime eventuel widget
        self.__view.focusWidget() # reprend le focus sur la fenetre principal
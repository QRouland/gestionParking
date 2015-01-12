import sys

from PyQt4 import QtGui

from src.c.Borne import Borne
from src.c.DetailsPlaces import DetailsPlaces
from src.c.log.log import Log
from src.c.log.log import lvl
from src.c.CreaParking import CreaParking
from src.v.MyQMainWindow import MyQMainWindow
from src.v.Ui_MainWindow import Ui_MainWindow

__author__ = 'sidya'


class Main:
    def __init__(self):
        # Init des logs
        self.lvl = lvl()  # Public : Acces au constante
        self.__log = Log()

        # Parking
        self.__parkings = []

        app = QtGui.QApplication(sys.argv)

        self.__view = MyQMainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__view)


        # connect
        self.__ui.comboBox.currentIndexChanged['QString'].connect(self.selectParking)
        self.__ui.btn_creer.clicked.connect(self.creerParking)
        self.__ui.btn_supprimer.clicked.connect(self.rmParking)
        self.__ui.btn_details.clicked.connect(self.detailsPlacesParking)
        self.__ui.btn_borne.clicked.connect(self.afficherBorne)



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
        self.__ui.placesParNiveau.clear()
        self.__ui.placesDispo.clear()
        self.__ui.placesSuperAbo.clear()
        if self.__ui.comboBox.count() > 1:
            print(self.__ui.comboBox.count())
            self.__ui.nom.setText(self.__parkings[self.__ui.comboBox.currentIndex() - 1].nom)
            self.__ui.placesParNiveau.setText(str(self.__parkings[self.__ui.comboBox.currentIndex() - 1].nbPlaces))
            self.__ui.placesDispo.setText(
                str(self.__parkings[self.__ui.comboBox.currentIndex() - 1].nbPlacesLibresParking))
            self.__ui.placesSuperAbo.setText("lol")


    def creerParking(self):
        self.__view.hide()
        self.__widgetCourant = CreaParking(self)

    def addParking(self, parking):
        self.__parkings.append(parking)

    def modifParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            self.__widgetCourant = ModifParking(self, self.__parkings[self.__ui.comboBox.currentIndex() - 1])

    def rmParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            result = QtGui.QMessageBox.question(self.__view,
                                                "Confirmer Supression...",
                                                "Etes vous sur de vouloir supprimer ?\n"
                                                "(La suppression sera définitive)",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if result == QtGui.QMessageBox.Yes:
                self.__parkings.remove(self.__parkings[self.__ui.comboBox.currentIndex() - 1])
            self.__view.hide()
            self.showWindow()

    def detailsPlacesParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            self.__widgetCourant = DetailsPlaces(self, self.__parkings[self.__ui.comboBox.currentIndex() - 1])

    def afficherBorne(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            self.__widgetCourant = Borne(self, self.__parkings[self.__ui.comboBox.currentIndex() - 1])


    def showWindow(self):
        self.majListeParking()
        self.__view.show()
        self.__widgetCourant = None  # supprime eventuel widget
        self.__view.focusWidget()  # reprend le focus sur la fenetre principal
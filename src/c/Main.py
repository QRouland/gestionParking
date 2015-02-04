import sys

from PyQt4 import QtGui

from src.c.Borne import Borne
from src.c.DetailsPlaces import DetailsPlaces
from src.c.log.log import Log
from src.c.log.log import lvl
from src.c.CreaParking import CreaParking
from src.m.Service import Service
from src.m.Parking import Parking
from src.m.Service import TypeService
from src.m.connexionBDD import connexionBDD
from src.v.MyQMainWindow import MyQMainWindow
from src.v.Ui_MainWindow import Ui_MainWindow

__author__ = 'sidya'


class Main:
    def __init__(self):
        # Init des logs
        self.lvl = lvl()  # Public : Acces au constante
        self.__log = Log()

        app = QtGui.QApplication(sys.argv)

        self.__view = MyQMainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__view)


        # connect
        self.__ui.comboBox.currentIndexChanged['QString'].connect(self.selectParking)
        self.__ui.btn_creer.clicked.connect(self.creerParking)
        self.__ui.btn_supprimer.clicked.connect(self.rmParking)
        self.__ui.btn_details.clicked.connect(self.detailsPlacesParking)
        self.__ui.btn_borne.clicked.connect(self.afficherBornes)
        self.__ui.actionNouveau_2.triggered.connect(self.nouveau)
        self.__ui.actionSauvegarder.triggered.connect(self.sauver)
        self.__ui.actionCharger.triggered.connect(self.charger)
        self.__ui.actionQuitter.triggered.connect(self.quitter)



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
        for p in Parking.getAllActif():
            self.__ui.comboBox.addItem(p.nom)

    def selectParking(self):
        #onglet detail parking
        self.__ui.nom.clear()
        self.__ui.placesParNiveau.clear()
        self.__ui.placesDispo.clear()
        self.__ui.placesSuperAbo.clear()
        if self.__ui.comboBox.count() > 1:
            p = Parking.getAllActif()
            self.__ui.nom.setText(p[self.__ui.comboBox.currentIndex() - 1].nom)
            self.__ui.placesParNiveau.setText(str(p[self.__ui.comboBox.currentIndex() - 1].nbPlaces))
            self.__ui.placesDispo.setText(
                str(p[self.__ui.comboBox.currentIndex() - 1].nbPlacesLibresParking))
            self.__ui.placesSuperAbo.setText(str(p[self.__ui.comboBox.currentIndex() - 1].nbSuperAbo))
            self.__ui.btn_details.setDisabled(False)
            self.__ui.btn_supprimer.setDisabled(False)
            self.__ui.btn_borne.setDisabled(False)
        else:
            self.__ui.btn_details.setDisabled(True)
            self.__ui.btn_supprimer.setDisabled(True)
            self.__ui.btn_borne.setDisabled(True)

        #onglet Service
        self.__ui.comboBox_livraison.clear()
        self.__ui.comboBox_entretien.clear()
        self.__ui.comboBox_maintenance.clear()
        if self.__ui.comboBox.count() > 1:
            for s in Service.getAllEnCours(p[self.__ui.comboBox.currentIndex() - 1]):
                if s.typeService == TypeService.LIVRAISON :
                    self.__ui.comboBox_livraison.addItem(str(s.id))
                if s.typeService == TypeService.ENTRETIEN :
                    self.__ui.comboBox_entretien.addItem(str(s.id))
                if s.typeService == TypeService.MAINTENANCE :
                    self.__ui.comboBox_maintenance.addItem(str(s.id))

            #Onglet Stats


    def creerParking(self):
        self.__view.hide()
        self.__widgetCourant = CreaParking(self)



    def rmParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            result = QtGui.QMessageBox.question(self.__view,
                                                "Confirmer Supression...",
                                                "Etes vous sur de vouloir supprimer ?\n"
                                                "(La suppression sera définitive)",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if result == QtGui.QMessageBox.Yes:
                Parking.remove(Parking.parkings[self.__ui.comboBox.currentIndex() - 1])
            self.__view.hide()
            self.showWindow()

    def detailsPlacesParking(self):
        if self.__ui.comboBox.currentIndex() != 0 :
            self.__view.hide()
            self.__widgetCourant = DetailsPlaces(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])

    def afficherBornes(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            Borne(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])
            Borne(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])

    def nouveau(self):
        result = QtGui.QMessageBox.question(self.__view,
                                                "Confirmer Nouveau...",
                                                "Etes vous sur de vouloir supprimer ?\n"
                                                "(Toutes données non sauvegardées seront perdues)",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            c = connexionBDD()
            c.initialisationBDD()
            c.seDeconnecter()
            Parking.removeAllRam()
            self.majListeParking()

    def charger(self):
        path = QtGui.QFileDialog.getOpenFileName(self.__view,"Charger",".")
        if path:
            connexionBDD.charger(path)
        self.majListeParking()

    def sauver(self):
        path = QtGui.QFileDialog.getSaveFileName(self.__view,"Sauvegarder",".")
        if path:
            connexionBDD.sauver(path)
        self.majListeParking()

    def quitter(self):
        self.__view.close()

    def showWindow(self):
        self.majListeParking()
        self.__view.show()
        self.__widgetCourant = None  # supprime eventuel widget
        Borne.bornes = []
        self.__view.focusWidget()  # reprend le focus sur la fenetre principal
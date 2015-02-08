"""
    Contrileur Principal de l'application
"""

import sys

from PyQt4 import QtGui, QtCore
import datetime
from src.c.Teleporteur import Teleporteur

from src.c.Borne import Borne
from src.c.Parking import CreaParking, DetailsPlaces
from src.c.utils.connexionBDD import connexionBDD
from src.c.utils.log import Log
from src.c.utils.log import lvl
from src.m.Abonnement import Client
from src.m.Parking import Parking, Placement
from src.m.Service import Service, TypeService
from src.v.MyQt import MyQMainWindow
from src.v.Ui_Admin import Ui_MainWindow


## Controleur principal de l'application administration
class Main:
    ## Contructeur
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
        self.__ui.btn_effectuer_entretien.clicked.connect(self.doEntretien)
        self.__ui.btn_effectuer_livraison.clicked.connect(self.doLivraison)
        self.__ui.btn_effectuer_maintenance.clicked.connect(self.doMaintenance)
        self.__ui.actionNouveau_2.triggered.connect(self.nouveau)
        self.__ui.actionSauvegarder.triggered.connect(self.sauver)
        self.__ui.actionCharger.triggered.connect(self.charger)
        self.__ui.actionQuitter.triggered.connect(self.quitter)
        self.__ui.btn_modif_livraison.clicked.connect(self.majLivraison)



        # Chargement activité
        self.loadLastActivity()

        self.showWindow()
        sys.exit(app.exec_())

    ## Methode d'ecriture dans les logs
    # @param msg message a ecrire
    # @param lvl lvl du message (niveau d'importance)
    def activity(self, msg, lvl):
        self.__log.printL(msg, lvl)
        self.addItemActivite(self.activite.readlines()[-1])

    ## Chargement des derniers log
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

    ## Mise a jour de la liste des parking
    def majListeParking(self):
        self.__ui.comboBox.clear()
        self.__ui.comboBox.addItem("Selectionner un parking")
        for p in Parking.getAllActif():
            self.__ui.comboBox.addItem(p.nom)

    ## Action a réaliser lorque un parking est selectionné
    def selectParking(self):
        # onglet detail parking
        self.__ui.nom.clear()
        self.__ui.placesParNiveau.clear()
        self.__ui.placesDispo.clear()
        self.__ui.placesSuperAbo.clear()
        if self.__ui.comboBox.count() > 1:
            p = Parking.getAllActif()
            self.activity("Parking selectionné : " + str(p[self.__ui.comboBox.currentIndex() - 1]), self.lvl.INFO)
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
        self.__ui.dateTimeEdit.clear()
        self.__ui.lieuLineEdit.clear()
        self.__serviceLivraisons = []
        self.__serviceEntretien = []
        self.__serviceMaintenance = []
        if self.__ui.comboBox.count() > 1:
            for s in Service.getAllEnCours(p[self.__ui.comboBox.currentIndex() - 1]):
                if s.typeService == TypeService.LIVRAISON:
                    self.__serviceLivraisons.append(s)
                    self.__ui.comboBox_livraison.addItem(str(s.info))
                    time = QtCore.QDateTime(datetime.datetime.fromtimestamp(s.dateService))
                    self.__ui.dateTimeEdit.setDateTime(time)
                    self.__ui.lieuLineEdit.setText(str(s.lieu))

                if s.typeService == TypeService.ENTRETIEN:
                    self.__serviceEntretien.append(s)
                    self.__ui.comboBox_entretien.addItem(str(s.info))
                if s.typeService == TypeService.MAINTENANCE:
                    self.__serviceMaintenance.append(s)
                    self.__ui.comboBox_maintenance.addItem(str(s.info))

        #Onglet Stats
        self.__ui.labelNbAbo.setText(str(Client.nbAbo()))
        self.__ui.labelNbSuperAbo.setText(str(Client.nbSuperAbo()))
        self.__ui.labelMoySta.setText(str(Placement.dureeMoyPlacement()))

    ## Gestion de la realisation d'une maintenance
    def doMaintenance(self):
        if len(self.__serviceMaintenance) > 0:
            try:
                s = self.__serviceMaintenance[self.__ui.comboBox_maintenance.currentIndex()]
                s.doService()
                self.activity("Livraision reussit : " + str(s), self.lvl.INFO)
            except Exception as e:
                self.activity("Livraision echoue    : " + str(e), self.lvl.FAIL)
                self.error("Livraision echoué.")
            self.selectParking()

    ## Gestion de la realisation d'un entrerien
    def doEntretien(self):
        if len(self.__serviceEntretien) > 0:
            try:
                s = self.__serviceEntretien[self.__ui.comboBox_entretien.currentIndex()]
                s.doService()
                self.activity("Entretien reussit : " + str(s), self.lvl.INFO)
            except Exception as e:
                self.activity("Entretien echoue " + str(e), self.lvl.FAIL)
                self.error("Entretien echoué.")
            self.selectParking()

    ## Gestion de la realisation d'une livraison
    def doLivraison(self):
        if len(self.__serviceLivraisons) > 0:
            try:
                s = self.__serviceLivraisons[self.__ui.comboBox_livraison.currentIndex()]
                s.doService()
                Teleporteur.teleporterVersSortie(s.placement)
                self.activity("Livraison reussit : " + str(s), self.lvl.INFO)
            except Exception as e:
                self.activity("Livraison echoue : " + str(e), self.lvl.FAIL)
                self.error("Livraison echoué.")
            self.selectParking()

    ## Gestion de la mise a our d'une livraison
    def majLivraison(self):
        if len(self.__serviceLivraisons) > 0:
            try:
                s = self.__serviceLivraisons[self.__ui.comboBox_livraison.currentIndex()]
                s.maj(self.__ui.dateTimeEdit.dateTime().toPyDateTime().timestamp(),
                      self.__ui.lieuLineEdit.text())
                self.activity("Maj Livraison reussit : " + str(s), self.lvl.INFO)
            except Exception as e:
                self.activity("Maj Livraison echoue : " + str(e), self.lvl.FAIL)
                self.error("Maj Livraison echoué.")
            self.selectParking()

    ## Gestion de l'ouverture d'une fenetre de CreaParking
    def creerParking(self):
        self.__view.hide()
        self.__widgetCourant = CreaParking(self)

    ## Suppresion d'un parking
    def rmParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            result = QtGui.QMessageBox.question(self.__view,
                                                "Confirmer Supression...",
                                                "Etes vous sur de vouloir supprimer ?\n"
                                                "(La suppression sera définitive)",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if result == QtGui.QMessageBox.Yes:
                try:
                    Parking.remove(Parking.parkings[self.__ui.comboBox.currentIndex() - 1])
                    self.activity("Supression parking reussit", self.lvl.INFO)
                except Exception as e:
                    self.activity("Suppression parking echoue : " + str(e), self.lvl.FAIL)
                    self.error("Suppression parking echoué.")
            self.__view.hide()
            self.showWindow()

    ## Affichage d'une fentre DetailsPlaces des places d'un parking
    def detailsPlacesParking(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            self.__widgetCourant = DetailsPlaces(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])

    ## Gestion affichage des Borne
    def afficherBornes(self):
        if self.__ui.comboBox.currentIndex() != 0:
            self.__view.hide()
            Borne(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])
            Borne(self, Parking.getAllActif()[self.__ui.comboBox.currentIndex() - 1])

    ## Gestion reinitilaisation de la BD
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

    ## gestion du chargement d'une BD enregistre dans un fichier
    def charger(self):
        path = QtGui.QFileDialog.getOpenFileName(self.__view, "Charger", ".")
        if path:
            try:
                connexionBDD.charger(path)
                self.activity("Le chargement a reussit", self.lvl.INFO)
            except Exception as e:
                self.activity("Le chargement a echoue : " + str(e), self.lvl.FAIL)
                self.error("Le chargement a echoué.")
        self.majListeParking()

    ## Gestion suvegarde de la BD dans un fichier
    def sauver(self):
        path = QtGui.QFileDialog.getSaveFileName(self.__view, "Sauvegarder", ".")
        if path:
            try:
                connexionBDD.sauver(path)
                self.activity("La sauvegarde a reussit", self.lvl.INFO)
            except Exception as e:
                self.activity("La sauvegarde a echoue : " + str(e), self.lvl.FAIL)
                self.error("La sauvegarde a echoué.")
        self.majListeParking()

    ## Gestion quitter
    def quitter(self):
        self.__view.close()

    ## Gestion affichage Main
    def showWindow(self):
        self.activity("Chargement de la fenetre principal", self.lvl.INFO)
        self.majListeParking()
        self.__view.show()
        self.__widgetCourant = None  # supprime eventuel widget
        Borne.bornes = []
        self.__view.focusWidget()  # reprend le focus sur la fenetre principal

    ## Gestion affichage QDialog d'erreur
    # @param msg le message d'erreur
    def error(self, msg):
        QtGui.QMessageBox.warning(self.__widgetCourant,
                                  "Erreur ...",
                                  msg
        )
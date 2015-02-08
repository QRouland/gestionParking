"""
    Module Controleur de la vue des bornes permettant l'accès au parking
"""

from PyQt4 import QtGui, QtCore
from src.c.Teleporteur import Teleporteur
from src.m.Parking import Placement
from src.m.Abonnement import Client
from src.m.Abonnement import TypeAbonnement
from src.m.Service import Service, TypeService
from src.v.Camera import Camera
from src.v.MyQt import MyQWidget
from src.v.Ui_User import Ui_Borne


##Controleur de la vue des bornes permettant l'accès au parking
class Borne:
    bornes = []

    ## Met a jour l'affichages du nombres de places dispo sur toutes les bornes
    @staticmethod
    def MajBornes():
        for b in Borne.bornes:
            b.MajBorne()

    ## Met a jour l'affichage du nombre de places dispo sur la borne courante
    def MajBorne(self):
        self.__ui.lcdNumber.display(self.__parking.nbPlacesLibresParking)

    ## Contructeur du controleur de borne
    # @param main Controleur parent Main
    # @param parking Parking auquel la borne est associé
    def __init__(self, main, parking):
        self.__nomBorne = "Borne " + str(len(self.bornes) + 1)
        self.__parking = parking
        self.__main = main
        self.__main.activity("Affichage " + self.__nomBorne, self.__main.lvl.INFO)

        self.__w = MyQWidget(self.__main)
        self.__ui = Ui_Borne()
        self.__ui.setupUi(self.__w)

        # connect
        self.__ui.btn_quitter.clicked.connect(self.quitter)
        self.__ui.btn_Voiture.clicked.connect(self.newVoiture)
        self.__ui.btn_annuler.clicked.connect(self.nonVoiture)
        self.__ui.btn_validerID.clicked.connect(self.identification)
        self.__ui.btn_valider_abo.clicked.connect(self.abo)
        self.__ui.btn_desabo.clicked.connect(self.desabo)
        self.__ui.btn_garer.clicked.connect(self.garer)
        self.__ui.btn_recuperer.clicked.connect(self.recuperer)
        self.__ui.pushButton.clicked.connect(self.payer)

        # Validator
        validatorText = QtGui.QRegExpValidator(QtCore.QRegExp('^([a-zA-Z\'àâéèêôùûçñãõÀÂÉÈÔÙÛÑÃÕÇ\s-]{2,30})$'))
        validatorCB = QtGui.QRegExpValidator(QtCore.QRegExp('^([0-9]*)$'))
        self.__ui.nomLineEdit.setValidator(validatorText)
        self.__ui.prenomLineEdit.setValidator(validatorText)
        self.__ui.lieuLineEdit_2.setValidator(validatorText)
        self.__ui.numeroCarteLineEdit.setValidator(validatorCB)

        self.__ui.label_aff.setStyleSheet("qproperty-alignment: AlignCenter; font-size: 28px")
        self.__ui.nomParking.setStyleSheet("qproperty-alignment: AlignCenter; font-size: 28px")
        self.nonVoiture()
        self.showWindow()
        self.__ui.nomParking.setText(self.__nomBorne + " - Parking : " + parking.nom)
        Borne.bornes.append(self)
        Borne.MajBornes()

    ## block l'ensmeble des éléments de  la fenetre
    def blockAll(self):
        self.__ui.box_abo.setDisabled(True)
        self.__ui.box_garer.setDisabled(True)
        self.__ui.box_id.setDisabled(True)
        self.__ui.box_recup.setDisabled(True)

        self.__ui.btn_Voiture.setDisabled(True)
        self.__ui.btn_annuler.setDisabled(True)
        self.__ui.btn_desabo.setDisabled(True)

    ## Met en etat initial de départ sans voiture
    def nonVoiture(self):
        self.__main.activity(self.__nomBorne + " : En Attente d'une voiture", self.__main.lvl.INFO)
        self.__ui.label_aff.setText("Dream park")
        self.__c = None
        self.__ui.box_abo.setDisabled(True)
        self.__ui.box_garer.setDisabled(True)
        self.__ui.box_id.setDisabled(True)
        self.__ui.box_recup.setDisabled(False)
        self.__ui.box_service.setDisabled(True)
        self.__ui.btn_Voiture.setDisabled(False)
        self.__ui.btn_desabo.setDisabled(True)
        self.__ui.btn_quitter.setDisabled(False)

        self.__ui.nomLineEdit.setText("")
        self.__ui.prenomLineEdit.setText("")
        self.__ui.numeroCarteLineEdit.setText("")
        self.__ui.checkBox.setChecked(False)
        self.__ui.lineEdit_id.setText("")
        self.__ui.numeroTicketLineEdit.setText("")
        self.__ui.labIdClient.setText("Non identifier")
        self.__ui.btn_valider_abo.setText("Valider")
        self.__ui.checkBox_Maintenance_2.setChecked(False)
        self.__ui.checkBox_Entretien_2.setChecked(False)
        self.__ui.checkBox_Livraison_2.setChecked(False)
        self.__ui.lieuLineEdit_2.setText("")
        self.__ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        Borne.MajBornes()

    ## Met en etat d'arrive de voiture detecte par la camera
    def newVoiture(self):
        self.__ui.btn_Voiture.setDisabled(True)
        self.__v_actuel = Camera.donnerVoiture()
        self.__main.activity(self.__nomBorne + " : Arrivee : " + str(self.__v_actuel), self.__main.lvl.INFO)
        self.__ui.box_abo.setDisabled(False)
        self.__ui.box_garer.setDisabled(False)
        self.__ui.box_id.setDisabled(False)
        self.__ui.box_recup.setDisabled(True)
        self.__ui.label_aff.setText("Bienvenue !")
        self.__ui.btn_quitter.setDisabled(True)

    ## Gestion de l'identification a partir d'un abo a partir de son id (lineedit)
    def identification(self):
        try:
            self.__c = Client(self.__ui.lineEdit_id.text())
            self.__ui.label_aff.setText("Bonjour " + str(self.__c.nom) + " " + str(self.__c.prenom))
            self.__ui.labIdClient.setText("Vous étes identifier")
            self.__ui.box_id.setDisabled(True)
            self.__ui.box_service.setDisabled(False)
            self.__ui.btn_desabo.setDisabled(False)
            self.__v_actuel.setClient(self.__c)
            self.__ui.nomLineEdit.setText(self.__c.nom)
            self.__ui.prenomLineEdit.setText(self.__c.prenom)
            self.__ui.numeroCarteLineEdit.setText(self.__c.cb)
            self.__ui.btn_valider_abo.setText("Modifier")
            self.__main.activity(self.__nomBorne + " : Mise a jour : " + str(self.__v_actuel), self.__main.lvl.INFO)
            self.__main.activity(self.__nomBorne + " : Identification : " + str(self.__c), self.__main.lvl.INFO)
        except IndexError:
            self.__ui.label_aff.setText("Echec identification")
            self.__ui.labIdClient.setText("Non identifier")
            self.__main.activity(self.__nomBorne + " : Identifiant Invalide", self.__main.lvl.INFO)
        except Exception as e:
            self.error("Une erreur est survenu lors de votre identification")
            self.__main.activity(self.__nomBorne + " : Erreur lors de l'indentification " + str(e),
                                 self.__main.lvl.FAIL)

    ## Gestion validation formulaire d'abonnement
    def abo(self):
        if self.__c != None:
            if self.__ui.checkBox.isChecked():
                self.__c.maj(str(self.__ui.nomLineEdit.text()),
                        str(self.__ui.prenomLineEdit.text()),
                        str(self.__ui.numeroCarteLineEdit.text()),
                        TypeAbonnement.SUPER_ABONNE)
            else:
                self.__c.maj(str(self.__ui.nomLineEdit.text()),
                        str(self.__ui.prenomLineEdit.text()),
                        str(self.__ui.numeroCarteLineEdit.text()),
                        TypeAbonnement.ABONNE)
            self.__ui.label_aff.setText("Mise a jour de votre abonnement effectué")
            self.__main.activity(self.__nomBorne + " : Mise à jour : " + str(self.__c), self.__main.lvl.INFO)
        else:
            if self.__ui.checkBox.isChecked():
                self.__c = Client(None,
                                  str(self.__ui.nomLineEdit.text()),
                                  str(self.__ui.prenomLineEdit.text()),
                                  str(self.__ui.numeroCarteLineEdit.text()),
                                  TypeAbonnement.SUPER_ABONNE)
            else:
                self.__c = Client(None,
                                  str(self.__ui.nomLineEdit.text()),
                                  str(self.__ui.prenomLineEdit.text()),
                                  str(self.__ui.numeroCarteLineEdit.text()),
                                  TypeAbonnement.ABONNE)

                self.__main.activity(self.__nomBorne + " : Ajout  : " + str(self.__c), self.__main.lvl.INFO)
            self.__ui.lineEdit_id.setText(self.__c.id)
            self.identification()
            self.__ui.label_aff.setText("Votre id membre est : " + self.__c.id)

    ## Gestion du desabonnment du client identifié
    def desabo(self):
        self.__c.desabo()
        self.__c = None
        self.__ui.nomLineEdit.setText("")
        self.__ui.prenomLineEdit.setText("")
        self.__ui.numeroCarteLineEdit.setText("")
        self.__ui.lineEdit_id.setText("")
        self.__ui.checkBox.setChecked(False)
        self.__ui.box_id.setDisabled(False)
        self.__ui.box_service.setDisabled(True)


    ## Gestion de la validation pour garer son vehicule
    def garer(self):
        placement = None
        if self.__c is None:
            p = self.__parking.recherchePlace(self.__v_actuel)
            if p is not None:
                placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)
        else:
            p = self.__parking.recherchePlace(self.__v_actuel)
            if p is not None:
                placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)

            # Si superAbo on cree une place sur mesure dans le cas ou acun est valide
            if p is None and self.__c.abonnement == TypeAbonnement.SUPER_ABONNE:
                placement = Teleporteur.teleporterVoitureSuperAbonne(self.__v_actuel, self.__parking)
                p = placement.place
                self.__main.activity(self.__nomBorne + " : Nouveau place SuperAbo  : " + str(p), self.__main.lvl.INFO)

            # Creation des service
            if p is not None:
                try :
                    if self.__ui.checkBox_Livraison_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.LIVRAISON,
                                    self.__ui.dateTimeEdit.dateTime().toPyDateTime().timestamp(),
                                    self.__ui.lieuLineEdit_2.text())
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
                    if self.__ui.checkBox_Entretien_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.ENTRETIEN)
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
                    if self.__ui.checkBox_Maintenance_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.MAINTENANCE)
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
                except Exception :
                    self.__main.activity(self.__nomBorne + " : Echec creation service : " + str(s), self.__main.lvl.FAIL)
                    self.error("Erreur lors de la creation des Services")
        if placement is not None:
            self.nonVoiture()
            self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(placement), self.__main.lvl.INFO)
            self.ticketDepot(placement.id)
        else:
            self.__ui.label_aff.setText("Aucune Place Correspondante. Devenez Super Abonné!")
            self.__main.activity(self.__nomBorne + " : Pas de place dispo pour " + str(self.__v_actuel),
                                 self.__main.lvl.INFO)

    ## Gestion de recuperation une voiture avec le numero de ticket (lineedit)
    def recuperer(self):
        p = None
        try:
            p = Placement(self.__ui.numeroTicketLineEdit.text())
        except IndexError:
            self.__ui.label_aff.setText("Mauvais numero de ticket")
            self.__main.activity(self.__nomBorne + " :  Mauvais numero de ticket", self.__main.lvl.INFO)
        try:
            Teleporteur.teleporterVersSortie(p)
        except  Exception as e :
            self.__ui.label_aff.setText("Voiture déjà recuperée")
            self.__main.activity(self.__nomBorne + " :  Recuperation déjà effectué : " + str(p), self.__main.lvl.INFO)
        if p.place.estSuperAbo :
            p.place.supprimer()
            self.__main.activity(self.__nomBorne + " : Suppresion place SuperAbo  : " , self.__main.lvl.INFO)
        if p is not None:
            if p.voiture.client != "NULL":
                self.ticketRetrait(p, Service.getAllServicePlacement(p))
                self.__main.activity(self.__nomBorne + " : Recuperation Abo : " + str(p), self.__main.lvl.INFO)
                self.nonVoiture()
            else:
                self.__placementAPayer = p
                self.blockAll()
                self.__ui.box_recup.setDisabled(False)
                self.__ui.numeroTicketLineEdit.setDisabled(True)
                self.__ui.btn_quitter.setDisabled(True)
                self.__ui.pushButton.setDisabled(False)
                self.__ui.numeroTicketLineEdit.setDisabled(True)

    ## Gestion du payeent
    def payer(self):
        self.nonVoiture()
        self.__ui.btn_quitter.setDisabled(False)
        self.__ui.btn_Voiture.setDisabled(False)
        self.ticketRetrait(self.__placementAPayer, Service.getAllServicePlacement(self.__placementAPayer))
        self.__main.activity(self.__nomBorne + " : Recuperation Anonyme : " + str(self.__placementAPayer), self.__main.lvl.INFO)

    ## generation ticket depot
    def ticketDepot(self, id):
        QtGui.QMessageBox.information(self.__w,
                                      "Ticket",
                                      "Votre numero ticket : " + str(id)
        )

    ## generation ticket retrait
    def ticketRetrait(self, placement, services):
        if placement.voiture.client == "NULL":
            prix = placement.place.typePlace.prix
            s = "Prix :  " + str(prix) + "€" + \
                "\nMerci de votre confiance! Bonne journée !"
        else:
            prix = placement.place.typePlace.prix - placement.place.typePlace.prix * 10 / 100
            s = "Prix :  " + str(placement.place.typePlace.prix) + "- 10%  = " + \
                str(prix) + "€"
            for service in services:
                if service.typeService == TypeService.MAINTENANCE:
                    name = "Maintenance"
                elif service.typeService == TypeService.ENTRETIEN:
                    name = "Entretien"
                else:
                    name = "Autre Service"
                if service.estRealise:
                    s += "\nService : " + name + " + 2€"
                else:
                    service.nonRealise()
                    s += "\nNous n'avons pas pu réaliser le service" + name + "."
                    s += "\nVeuillez nous excuser de la gène ocassionée."
            s += "\nLe Montant sera débiter automatiquement sur votre compte."
            s += "\nMerci de votre confiance! Bonne journée !"
        QtGui.QMessageBox.information(self.__w,
                                      "Ticket",
                                      str(s)
        )

    ## Gestion affichage de la vue borne
    def showWindow(self):
        self.__w.show()

    ## Gestion de sortie de la vue borne
    def quitter(self):
        self.__main.activity(self.__nomBorne + " :  Quitter", self.__main.lvl.INFO)
        self.__main.showWindow()

    ## Generation Qdialog d'erreur
    # @param msg message d'erreur a afficher
    def error(self, msg):
        QtGui.QMessageBox.warning(self._w,
                                  "Erreur ...",
                                  "Erreur lors de la création du parking ...\n" +
                                  msg
        )

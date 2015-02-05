from PyQt4 import QtGui, QtCore

from src.c.Teleporteur import Teleporteur
from src.m.Parking import Placement
from src.m.Client import Client
from src.m.Service import Service, TypeService
from src.m.Client import TypeAbonnement
from src.v.Camera import Camera
from src.v.MyQWidget import MyQWidget
from src.v.Ui_Borne import Ui_Borne


__author__ = 'sidya'


class Borne:
    """
    Controleur de la vue des bornes permettant l'accès au parking
    """
    bornes = []

    @staticmethod
    def MajBornes():
        for b in Borne.bornes:
            b.MajBorne()

    def MajBorne(self):
        self.__ui.lcdNumber.display(self.__parking.nbPlacesLibresParking)

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
        self.__ui.btn_garer.clicked.connect(self.garer)
        self.__ui.btn_recuperer.clicked.connect(self.recuperer)



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


    def blockAll(self):
        self.__ui.box_abo.setDisabled(True)
        self.__ui.box_garer.setDisabled(True)
        self.__ui.box_id.setDisabled(True)
        self.__ui.box_recup.setDisabled(True)

        self.__ui.btn_Voiture.setDisabled(True)
        self.__ui.btn_annuler.setDisabled(True)
        self.__ui.btn_desabo.setDisabled(True)

    def nonVoiture(self):
        """
        Met en etat initial de départ sans voiture
        :return:
        """
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

        self.__ui.nomLineEdit.setText("")
        self.__ui.prenomLineEdit.setText("")
        self.__ui.numeroCarteLineEdit.setText("")
        self.__ui.checkBox.setChecked(False)
        self.__ui.lineEdit_id.setText("")
        self.__ui.numeroTicketLineEdit.setText("")
        self.__ui.labIdClient.setText("Non identifier")
        Borne.MajBornes()

    def newVoiture(self):
        """
        Meten etat d'arrive de voiture detecte par la camera
        :return:
        """
        self.__ui.btn_Voiture.setDisabled(True)
        self.__v_actuel = Camera.donnerVoiture()
        self.__main.activity(self.__nomBorne + " : Arrivee : " + str(self.__v_actuel), self.__main.lvl.INFO)
        self.__ui.box_abo.setDisabled(False)
        self.__ui.box_garer.setDisabled(False)
        self.__ui.box_id.setDisabled(False)
        self.__ui.box_recup.setDisabled(True)
        self.__ui.label_aff.setText("Bienvenue !")


    def identification(self):
        """
        Gestion de l'identification a partir d'un abo a partir de son id (lineedit)
        :return:
        """
        try:
            self.__c = Client(self.__ui.lineEdit_id.text())
            self.__ui.label_aff.setText("Bonjour " + str(self.__c.nom) + " " + str(self.__c.prenom))
            self.__ui.labIdClient.setText("Vous étes identifier")
            self.__ui.box_id.setDisabled(True)
            self.__ui.box_service.setDisabled(False)
            self.__ui.btn_desabo.setDisabled(False)
            self.__v_actuel.setClient(self.__c)
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

    def abo(self):
        """
        Gestion validation formulaire d'abonnement
        :return:
        """
        if self.__c != None:
            self.__c.maj(self.__ui.nomLineEdit,
                         self.__ui.prenomLineEdit,
                         "",
                         TypeAbonnement.SUPER_ABONNE)
            self.__ui.label_aff.setText("Mise a jour de votre abonnement effectué")
            self.__main.activity(self.__nomBorne + " : Mise à jour : " + str(self.__c), self.__main.lvl.INFO)
        else:
            if self.__ui.checkBox.isChecked():
                self.__c = Client(None,
                                  str(self.__ui.nomLineEdit.text()),
                                  str(self.__ui.prenomLineEdit.text()),
                                  "",
                                  TypeAbonnement.SUPER_ABONNE)
            else:
                self.__c = Client(None,
                                  str(self.__ui.nomLineEdit.text()),
                                  str(self.__ui.prenomLineEdit.text()),
                                  "",
                                  TypeAbonnement.ABONNE)
                self.identification()
                self.__main.activity(self.__nomBorne + " : Ajout  : " + str(self.__c), self.__main.lvl.INFO)
                self.__ui.label_aff.setText("Votre id membre est : " + self.__c.id)
            self.__ui.lineEdit_id.setText(self.__c.id)


    def garer(self):
        """
        Gestion de la validation de garer son vehicule
        :return:
        """
        placement = None
        if self.__c is None:
            p = self.__parking.recherchePlace(self.__v_actuel)
            if p is not None:
                placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)
        else:
            if self.__c.abonnement != TypeAbonnement.SUPER_ABONNE:
                p = self.__parking.recherchePlace(self.__v_actuel)
                if p is not None:
                    placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)
                    if self.__ui.checkBox_Livraison_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.LIVRAISON)
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
                    if self.__ui.checkBox_Entretien_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.ENTRETIEN)
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
                    if self.__ui.checkBox_Maintenance_2.isChecked():
                        s = Service(None, self.__c, placement, TypeService.MAINTENANCE)
                        self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(s), self.__main.lvl.INFO)
            else:
                placement = Teleporteur.teleporterVoitureSuperAbonne(self.__v_actuel, self.__parking)
        if placement is not None:
            self.nonVoiture()
            self.ticketDepot(placement.id)
            self.__main.activity(self.__nomBorne + " : Nouveau  : " + str(placement), self.__main.lvl.INFO)
        else:
            self.__ui.label_aff.setText("Aucune Place Correspondante. Devenez Super Abonné!")
            self.__main.activity(self.__nomBorne + " : Pas de place dispo pour " + str(self.__v_actuel),
                                 self.__main.lvl.INFO)


    def recuperer(self):
        """
        Essaie de recuperer une voiture avec le numero de ticket (lineedit)
        :return:
        """
        p = None
        try:
            p = Placement(self.__ui.numeroTicketLineEdit.text())
        except IndexError:
            self.__ui.label_aff.setText("Mauvais numero de ticket")
            self.__main.activity(self.__nomBorne + " :  Mauvais numero de ticket", self.__main.lvl.INFO)
        try:
            Teleporteur.teleporterVersSortie(p)
        except  Exception:
            self.__ui.label_aff.setText("Voiture déjà recuperé")
            self.__main.activity(self.__nomBorne + " :  Recuperation déjà effectué : " + str(p), self.__main.lvl.INFO)
        if p is not None:
            self.nonVoiture()
            self.ticketRetrait(p, Service.getAllServicePlacement(p))
            self.__main.activity(self.__nomBorne + " : Recuperation  : " + str(p), self.__main.lvl.INFO)

    def ticketDepot(self, id):
        QtGui.QMessageBox.information(self.__w,
                                      "Ticket",
                                      "Votre numero ticket : " + str(id)
        )

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

                if service.estRealiser():
                    s += "\nService : " + name + " + 2€"
                else:
                    s += "\nNous n'avons pas pu réaliser le service" + name + "."
                    s += "\nVeuillez nous excuser de la gène ocassionée."
            s += "Le Montant sera débiter automatiquement sur votre compte."
            s += "\nMerci de votre confiance! Bonne journée !"
        QtGui.QMessageBox.information(self.__w,
                                      "Ticket",
                                      str(s)
        )


    def showWindow(self):
        """
        Gestion affichage de la vue borne
        :return:
        """
        self.__w.show()
        self.__child = None  # supprime l'eventuel widget enfant
        self.__w.focusWidget()  # reprend le focus sur la fenetre

    def quitter(self):
        """
        Gestion de sortie de la vue borne
        :return:
        """
        self.__main.activity(self.__nomBorne + " :  Quitter", self.__main.lvl.INFO)
        self.__main.showWindow()


    def error(self, msg):
        """
        Qdialog message erreur
        :return:
        """
        QtGui.QMessageBox.warning(self._w,
                                  "Erreur ...",
                                  msg
        )
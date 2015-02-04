from PyQt4 import QtGui

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
        print(Borne.bornes)
        for b in Borne.bornes:
            b.MajBorne()

    def MajBorne(self):
        self.__ui.lcdNumber.display(self.__parking.nbPlacesLibresParking)

    def __init__(self, main, parking):
        self.__parking = parking
        self.__main = main
        self.__main.activity("Affichage Borne", self.__main.lvl.INFO)

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



        self.__ui.label_aff.setStyleSheet("qproperty-alignment: AlignCenter; font-size: 28px")
        self.__ui.nomParking.setStyleSheet("qproperty-alignment: AlignCenter; font-size: 28px")
        self.nonVoiture()
        self.showWindow()
        self.__ui.nomParking.setText("Borne " + str(len(self.bornes)+1) + " - Parking : " +parking.nom)
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
        try :
            self.__c = Client(self.__ui.lineEdit_id.text())
            self.__ui.label_aff.setText("Bonjour " + str(self.__c.nom) + " " + str(self.__c.prenom))
            self.__ui.labIdClient.setText("Vous étes identifier")
            self.__ui.box_id.setDisabled(True)
            self.__ui.box_service.setDisabled(False)
            self.__ui.btn_desabo.setDisabled(False)
        except Exception :
            self.__ui.label_aff.setText("Echec identification")
            self.__ui.labIdClient.setText("Non identifier")

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
            self.__ui.label_aff.setText("Votre id membre est : " + self.__c.id)
            self.__ui.lineEdit_id.setText(self.__c.id)
            self.identification()

    def garer(self):
        """
        Gestion de la validation de garer son vehicule
        :return:
        """
        id = None
        if self.__c is None:
            p = self.__parking.recherchePlace(self.__v_actuel)
            if p is not None:
                placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)
        else:
            if self.__c.abonnement != TypeAbonnement.SUPER_ABONNE:
                p = self.__parking.recherchePlace(self.__v_actuel)
                if p is not None :
                    placement = Teleporteur.teleporterVoiture(self.__v_actuel, p)
                    if self.__ui.checkBox_Livraison_2.isChecked():
                        Service(None, self.__c, placement, TypeService.LIVRAISON)
                    if self.__ui.checkBox_Entretien_2.isChecked():
                        Service(None, self.__c, placement, TypeService.ENTRETIEN)
                    if self.__ui.checkBox_Maintenance_2.isChecked():
                        Service(None, self.__c, placement, TypeService.MAINTENANCE)
            else:
                placement = Teleporteur.teleporterVoitureSuperAbonne(self.__v_actuel, self.__parking)
        if placement is not None:
            self.nonVoiture()
            self.ticketDepot(placement.id)
        else:
            self.__ui.label_aff.setText("Aucune Place Correspondante. Devenez Super Abonné!")


    def recuperer(self):
        """
        Essaie de recuperer une voiture avec le numero de ticket (lineedit)
        :return:
        """
        try :
            p = Placement.get(self.__ui.numeroTicketLineEdit.text())
            Teleporteur.teleporterVersSortie(p)
            self.nonVoiture()
            self.ticketDepot(id)
        except IndexError:
            self.__ui.label_aff.setText("Mauvais numero de ticket")

    def ticketDepot(self, id):
        QtGui.QMessageBox.information(self.__w,
                                        "Ticket",
                                        "Votre numero ticket : " + str(id)
        )

    def ticketRetrait(self):
        QtGui.QMessageBox.information(self.__w,
                                        "Ticket",
                                        "Merci de votre confiance! Bonne journée !"
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
        self.__main.showWindow()


    def error(self):
        """
        Qdialog message erreur
        :return:
        """
        QtGui.QMessageBox.warning(self.__w,
                                  "Erreur ...",
                                  "Une erreur est survenue ...")
        self.__w.hide()
        self.__main.showWindow()
from src.c.Teleporteur import Teleporteur
from src.m.Placement import Placement
from src.m.Client import Client
from src.m.TypeAbonnement import TypeAbonnement
from src.v.Camera import Camera
from PyQt4 import QtGui
from src.v.MyQWidget import MyQWidget
from src.v.Ui_Borne import Ui_Borne
__author__ = 'sidya'


class Borne:
    """
    Controleur de la vue de la borne permettant l'accès au parking
    """
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


        #Validator


        self.__ui.nomParking = parking.nom
        self.nonVoiture()
        self.showWindow()



    def nonVoiture(self):
        """
        Met en etat initial de départ sans voiture
        :return:
        """
        self.__c = None
        self.__ui.box_abo.setDisabled(True)
        self.__ui.box_garer.setDisabled(True)
        self.__ui.box_id.setDisabled(True)
        self.__ui.box_recup.setDisabled(False)

    def newVoiture(self):
        """
        Meten etat d'arrive de voiture detecte par la camera
        :return:
        """
        self.v_actuel = Camera.donnerVoiture()
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
        self.__c = Client.get(self.__ui.lineEdit_id.text())
        if self.__c != None :
            self.__ui.label_aff.setText("Bonjour " + str(self.__c.nom)+ " " + str(self.__c.prenom))
            #self.__ui.labIdClient.setText(str(self.__c))
            self.__ui.box_id.setDisabled(True)
        else :
            self.__ui.label_aff.setText("Echec identification")
            self.__ui.labIdClient.setText("Non identifier")

    def abo(self):
        """
        Gestion validation formaulaire d'abonnement
        :return:
        """
        if self.__c != None :
            self.__c.maj(self.__ui.nomLineEdit,
                                  self.__ui.prenomLineEdit,
                                  "",
                                  TypeAbonnement.SUPER_ABONNE)
            self.__ui.label_aff.setText("Mise a jour de votre abonnement effectué")
        else:
            if self.__ui.checkBox.isEnabled() :
                self.__c = Client(self.__ui.nomLineEdit,
                                  self.__ui.prenomLineEdit,
                                  "",
                                  TypeAbonnement.SUPER_ABONNE)
            else :
                self.__c = Client(self.__ui.nomLineEdit,
                                  self.__ui.prenomLineEdit,
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
        if self.__c is None:
            id = Teleporteur.teleporterVoiture(self.v_actuel,self.__parking.recherchePlace(self.v_actuel))
            self.__ui.label_aff.setText("Votre num ticket est : " + id)
        else:
            if self.__c.abonnement != TypeAbonnement.SUPER_ABONNE :
                Teleporteur.teleporterVoiture(self.v_actuel,self.__parking.recherchePlace(self.v_actuel))
            else:
                Teleporteur.teleporterVoirureSuperAbonne(self.v_actuel)


    def recuperer(self):
        """
        Essaie de recuperer une voiture avec le numero de ticket (lineedit)
        :return:
        """
        p = Placement.get(self.__ui.numeroTicketLineEdit.text())
        if p is None:
            self.__ui.label_aff.setText("Mauvais numero de ticket")
        else:
            Teleporteur.teleporterVersSortie(p)
            self.__ui.label_aff.setText("Bonne journée")



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
        self.__w.hide()
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
from src.v import Ui_Panneau, Ui_Borne, Camera
from src.m import Parking


__author__ = 'sidya'


class Acces:
    """
    Controleur Acces
    """
    def __init__(self):
        self.__parking = Parking()
        self.__camera = Camera()
        self.__borne = Ui_Borne()
        self.__panneau = Ui_Panneau()

    def actionnerCamera(self):
        return self.__camera.donnerVoiture()

    def majPanneau(self):
        self.__panneau.afficherNbPlaceDisponible()

    def lancerProcedureEntree(self, client):
        self.__borne.afficher("Inserer votre carte ou valider")


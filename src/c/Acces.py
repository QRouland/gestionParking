from src.v import Panneau, Borne, Camera
from src.c import Teleporteur
from src.m import Parking, Place


__author__ = 'sidya'


class Acces:
    def __init__(self):
        self.__parking = Parking()
        self.__camera = Camera()
        self.__borne = Borne()
        self.__panneau = Panneau()

    def actionnerCamera(self):
        return self.__camera.donnerVoiture()

    def majPanneau(self):
        self.__panneau.afficherNbPlaceDisponible()

    def lancerProcedureEntree(self,client):
        self.__borne.afficher("Inserer votre carte ou valider")

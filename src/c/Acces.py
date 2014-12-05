from src.v import Panneau, Borne, Camera
from src.c import Teleporteur
from src.m import Parking, Place


__author__ = 'sidya'


class Acces:
    def __init__(self):
        self.__borne = Borne()
        self.__panneau = Panneau()
        self.__parkings = {}
        self.__camera = Camera()
        self.__teleporteur = Teleporteur()
        self.__clients = {}

    def actionnerCamera(self, client):
        pass

    def actionnerPanneau(self):
        pass

    def lancerProcedureImmatr(self, voiture):
        pass
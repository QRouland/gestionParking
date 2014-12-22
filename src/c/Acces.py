from src.v import Panneau, Borne, Camera
from src.c import Teleporteur
from src.m import Parking, Place


__author__ = 'sidya'


class Acces:
    def __init__(self):
        self.__parkings = {}
        self.__clients = {}

    def actionnerCamera(self, client):
        pass

    def actionnerPanneau(self):
        pass

    def lancerProcedureImmatr(self, voiture):
        pass
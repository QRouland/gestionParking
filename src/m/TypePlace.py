__author__ = 'sidya'


class TypePlace:
    """
        Classe qui permet de définir un type de place
    """

    def __init__(self, h, l, nb):
        self.__hauteur = h
        self.__longueur = l
        self.__nb = nb

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def longueur(self):
        return self.__longueur

    @property
    def nb(self):
        return self.__nb

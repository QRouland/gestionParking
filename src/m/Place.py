__author__ = 'sidya'


class Place :
    def __init__(self,numero,niveau,longueur,hauteur):
        self.__numero = numero
        self.__niveau = niveau
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__estLibre = True
        self.__estReserver = False

    @property
    def estLibre(self):
        return self.__estLibre

    @property
    def estReserver(self):
        return self.__estReserver

    def dimValide(self,h,l):
        return h<self.__hauteur and l<self.__longueur

    def addPlacement(self, placement):
        pass


class TypePlace :
    def __init__(self,h,l,nb):
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


class ListeTypePlace :
    def __init__(self):
        self.l = []

    def add(self,h,l,nb):
        self.l.append(TypePlace(h,l,nb))

    @property
    def liste(self):
        return self.l
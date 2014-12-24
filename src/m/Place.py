import sys
import datetime

__author__ = 'sidya'


class Place:
    """
        Representation d'une place dans un parking
    """
    def __init__(self, numero, niveau, longueur, hauteur):
        self.__numero = numero
        self.__niveau = niveau
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__estLibre = True
        self.__estReserver = False
        self.__Placement = None
    @property
    def estLibre(self):
        return self.__estLibre

    @property
    def estReserver(self):
        return self.__estReserver

    def dimValide(self, h, l):
        return h < self.__hauteur and l < self.__longueur

    def reserver(self):
        if (self.__estReserver == True) :
            raise Exception("Place déjà reservé")
        self.__estReserver = True

    def nonReserver(self) :
        if (self.__estReserver == False):
            raise Exception("Impossible de mettre une place en non si elle n'est pas reservé de base")
        self.__estReserver = False

    def prendre(self, Placement):
        if (self.__Libre == True) :
            raise Exception("Place déjà prise")
        self.__estLibre = False
        self.__Placement = Placement

    def liberer(self) :
        if (self.__estLibre == False):
            raise Exception("Impossible de liberer une place vide")
        self.__estLibre = True


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


class ListeTypePlace:
    """
        Classe qui permet de définir une liste de type de place par niveau pour la création d'un parking
    """
    def __init__(self):
        self.l = []

    def add(self, h, l, nb):
        self.l.append(TypePlace(h, l, nb))

    @property
    def nbPlaceTotal(self):
        i = 0
        for t in self.l:
            i += t.nb
        return i

    @property
    def liste(self):
        return self.l


class Placement:
    def __init__(self,debut,fin):
        self.debut = debut
        self.fin = fin

    @property
    def estEnCours(self):
        return datetime.datetime < self.fin
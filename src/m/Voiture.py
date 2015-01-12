__author__ = 'sidya'

class Voiture:
    def __init__(self, longueur, hauteur, imma):
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__imma = imma
        self.__estDansParking = False

    @property
    def longueur(self):
        return self.__longueur

    @property
    def hauteur(self):
        return self.__hauteur

    def __str__(self):
        return "Voiture : hauteur " + str(self.__longueur) + ", largeur" + str(self.hauteur) + ", Imma : " + self.__imma +", est dans parking :" + str(self.__estDansParking)





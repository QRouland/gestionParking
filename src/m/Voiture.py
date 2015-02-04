from src.m.connexionBDD import connexionBDD

__author__ = 'sidya'

class Voiture:
    def __init__(self, id, idClient=None, longueur=None, hauteur=None, imma=None, estDansParking=False):
        if id is None :
            self.__idClient = idClient
            self.__longueur = longueur
            self.__hauteur = hauteur
            self.__imma = imma
            self.__estDansParking = estDansParking
            c = connexionBDD()
            c.execute("INSERT INTO voiture (longueur, hauteur, imma, estDansParking) VALUES (?,?,?,?)",
                      (self.__longueur, self.__hauteur, self.__imma, int(self.__estDansParking)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM voiture WHERE idVoiture='"+str(id)+"'")
            row = r.fetchone()
            if row is None :
                 raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__id = id
            self.__idClient = row["idClient"]
            self.__longueur = row["longueur"]
            self.__hauteur = row["hauteur"]
            self.__imma = row["imma"]
            self.__estDansParking = row["estDansParking"]


    @property
    def id(self):
        return self.__id

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def longueur(self):
        return self.__longueur

    @property
    def immatriculation(self):
        return self.__imma

    @property
    def estDansParking(self):
        return self.__estDansParking == True

    def __str__(self):
        return "[Voiture :" \
               " id = " + str(self.__id) + ", " \
               " longueur = " + str(self.__longueur) + ", " \
               " hauteur = " + str(self.__hauteur) + ", " \
               " imma = " + str(self.__imma) + ", " \
               " estDansParking = " + str(self.__estDansParking)+"]"
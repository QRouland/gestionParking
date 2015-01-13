from src.m.connexionBDD import connexionBDD

__author__ = 'sidya'

class Voiture:
    @staticmethod
    def get(id):
        c = connexionBDD()
        r = c.execute("SELECT * FROM voiture WHERE idVoiture='"+str(id)+"'")
        row = r.fetchone()
        if row is None :
             raise IndexError("Invalid id")
        c.seDeconnecter()
        return Voiture(id,row["longueur"],row["hauteur"],row["imma"], bool(row["estDansParking"]))


    def __init__(self, longueur, hauteur, imma, estDansParking):
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__imma = imma
        self.__estDansParking = estDansParking

        if id is None :
            c = connexionBDD()
            c.execute("INSERT INTO voiture (longueur,hauteur,imma, estDansParking) VALUES (?,?,?,?)",
                      (self.__longueur, self.__hauteur, self.__imma, int(self.__estDansParking)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            self.__id = id

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
        return self.__immatriculation

    @property
    def estDansParking(self):
        return self.__estDansParking == True

    def __str__(self):
        return "[Voiture :" \
               " longueur = " +self.__longueur + ", " \
               " hauteur = " +self.__hauteur + ", " \
               " imma = " +self.__imma + ", " \
               " estDansParking = " +self.__estDansParking + "]"
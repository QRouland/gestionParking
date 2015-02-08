"""
    Module qui implémente les classes representants d'une voiture de DreamPark.
"""
from src.c.utils.connexionBDD import connexionBDD
from src.m.Abonnement import Client

## Representation d'une Voiture de DreamPark
class Voiture:
    ## Constucteur Voiture
    # @param id Si None : Cree une Voiture dans la BD Sinon : tentative de récupération de la Voiture avec cet id dans la bd
    # @param client Si creation Client qui posséde la Voiture
    # @param longueur Si creation longueur de la Voiture
    # @param hauteur Si creation hauteur de la Voiture
    # @param imma Si creation imma de la Voiture
    def __init__(self, id, client=None, longueur=None, hauteur=None, imma=None):
        if id is None:
            if client is None:
                self.__client = "NULL"
                cl = "NULL"
            else:
                self.__client = client
                cl = self.__client.id
            self.__longueur = longueur
            self.__hauteur = hauteur
            self.__imma = imma
            c = connexionBDD()
            c.execute("INSERT INTO voiture (idClient,longueur, hauteur, imma) VALUES (?,?,?,?)",
                      (cl, self.__longueur, self.__hauteur, self.__imma))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM voiture WHERE idVoiture='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__id = id
            try:
                self.__client = Client(row["idClient"])
            except IndexError:
                self.__client = "NULL"
            self.__longueur = row["longueur"]
            self.__hauteur = row["hauteur"]
            self.__imma = row["imma"]

    ## Met a jour la possesion d'une Voiture par un Client
    # @param client Client qui posséde la voiture
    def setClient(self, client):
        self.__client = client
        c = connexionBDD()
        c.execute("UPDATE voiture SET idClient = '" + str(client.id) + "' WHERE idVoiture='" + str(self.id) + "'")
        c.seDeconnecter()

    ## propriete : id Voiture
    @property
    def id(self):
        return self.__id

    ## propriete : hauteur Voiture
    @property
    def hauteur(self):
        return self.__hauteur

    ## propriete : longueur Voiture
    @property
    def longueur(self):
        return self.__longueur

    ## propriete : immatriculation Voiture
    @property
    def immatriculation(self):
        return self.__imma

    ## propriete : Client possedant Voiture
    @property
    def client(self):
        return self.__client

    ## Representation d'une Voiture en chaine
    def __str__(self):
        return "[Voiture :" \
               " id = " + str(self.__id) + ", "+\
               " client = " + str(self.__client) + ", " +\
               " longueur = " + str(self.__longueur) + ", " +\
               " hauteur = " + str(self.__hauteur) + ", " +\
               " imma = " + str(self.__imma) + "]"
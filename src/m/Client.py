import random
import string
from src.m.connexionBDD import connexionBDD


__author__ = 'sidya'

class Client:
    @staticmethod
    def get(id):
        c = connexionBDD()
        r = c.execute("SELECT * FROM client WHERE idClient='"+str(id)+"'")
        row = r.fetchone()
        if row is None :
            raise IndexError("Invalid id")
        c.seDeconnecter()
        return Client(id, row["nom"],row["prenom"],row["adresse"], bool(row["typeAbonnement"]))


    def __init__(self,id, nom, prenom, adresse, typeAbonnement):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse

        if id is None:
            while True:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                             range(random.randint(1, 10)))
                try :
                    Client.get(id)
                except IndexError :
                    break

            self.__id = id
            c = connexionBDD()
            c.execute("INSERT INTO client (idClient, nom, prenom, adresse, typeAbonnement) VALUES (?,?,?,?,?)",
                      (str(self.__id), str(self.__nom), str(self.__prenom), "", str(self.__typeAbonnement)))
            self.__id = id
            c.seDeconnecter()
        else:
            self.__id = id

    @property
    def prenom(self):
        return self.__prenom

    @property
    def nom(self):
        return self.__nom

    @property
    def id(self):
        return self.__id

    @property
    def adr(self):
        return self.__adresse

    @property
    def abonnement(self):
        return self.__typeAbonnement

    def __str__(self):
        return "[Client :" \
               " id = " + str(self.__id) + ", " \
               " prenom = " + str(self.__prenom) + ", " \
               " nom = " + str(self.__nom) + ", " \
               " adresse = " + str(self.__adresse) + ", " \
               " typeAbonnement = " + str(self.__typeAbonnement) + "]"

class TypeAbonnement:
    ABONNE = 0
    SUPER_ABONNE = 1
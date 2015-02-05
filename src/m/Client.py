import random
import string

from src.m.connexionBDD import connexionBDD


__author__ = 'sidya'


class Client:
    def __init__(self, id, nom=None, prenom=None, adresse=None, typeAbonnement=None):
        if id is None:
            self.__nom = nom
            self.__prenom = prenom
            self.__typeAbonnement = typeAbonnement
            self.__adresse = adresse
            while True:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                             range(random.randint(1, 10)))
                try:
                    Client(id)
                except IndexError:
                    break
            self.__id = id
            c = connexionBDD()
            c.execute("INSERT INTO client (idClient, nom, prenom, adresse, typeAbonnement) VALUES (?,?,?,?,?)",
                      (str(self.__id), str(self.__nom), str(self.__prenom), "", str(self.__typeAbonnement)))
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM client WHERE idClient='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__id = id
            self.__nom = row["nom"]
            self.__prenom = row["prenom"]
            self.__typeAbonnement = row["typeAbonnement"]
            self.__adresse = row["adresse"]

    def maj(self, nom, prenom, adresse, typeAbonnement):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse
        c = connexionBDD()
        c.execute("UPDATE client SET nom = ?, prenom = ?, adresse = ?, typeAbonnement = ? WHERE idClient = ?",
                  (str(self.__nom), str(self.__prenom), "", str(self.__typeAbonnement), str(self.__id)))
        c.seDeconnecter()

    def desabo(self):
        c = connexionBDD()
        c.execute("DELETE FROM client WHERE idClient ='" + str(id) + "'")
        c.seDeconnecter()


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
                                                                                                             " adresse = " + str(
            self.__adresse) + ", " \
                              " typeAbonnement = " + str(self.__typeAbonnement) + "]"


class TypeAbonnement:
    ABONNE = 0
    SUPER_ABONNE = 1
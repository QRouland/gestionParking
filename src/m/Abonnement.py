"""
    Module qui implémente les classes representants les Abonnements de DreamPark.
"""
import random
import string
from src.c.utils.connexionBDD import connexionBDD

## Représentation d'un Client de DreamPark
class Client:
    ##
    #    Constructeur du Client
    #    @param id Si None : Création du  Client dans la bd a l'aide des autres parametres.
    #                Sinon  : tentative de récupération du client avec cet id dans la bd
    #    @param nom nom du Client si creation
    #    @param prenom prenom du Client si creation
    #    @param cb cb du Client si creation
    #    @param typeAbonnement typeabonnement du client si creation
    def __init__(self, id, nom=None, prenom=None, cb=None, typeAbonnement=None):

        if id is None:
            self.__nom = nom
            self.__prenom = prenom
            self.__typeAbonnement = typeAbonnement
            self.__cb = cb
            while True:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                             range(random.randint(1, 10)))
                try:
                    Client(id)
                except IndexError:
                    break
            self.__id = id
            c = connexionBDD()
            c.execute("INSERT INTO client (idClient, nom, prenom, cb, typeAbonnement) VALUES (?,?,?,?,?)",
                      (str(self.__id), str(self.__nom), str(self.__prenom), str(self.__cb), str(self.__typeAbonnement)))
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
            self.__cb = row["cb"]

    ##  Mise a jour du Client
    #   @param nom nouveau nom
    #   @param prenom nouveau prenom
    #   @param cb nouveau cb
    #   @param typeAbonnement nouveau TypeAbonnement
    def maj(self, nom, prenom, cb, typeAbonnement):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__cb = cb
        c = connexionBDD()
        c.execute("UPDATE client SET nom = ?, prenom = ?, cb = ?, typeAbonnement = ? WHERE idClient = ?",
                  (str(self.__nom), str(self.__prenom), "", str(self.__typeAbonnement), str(self.__id)))
        c.seDeconnecter()

    ## Desabonne le Client en le supprimant
    def desabo(self):
        c = connexionBDD()
        c.execute("DELETE FROM client WHERE idClient ='" + str(self.__id) + "'")
        c.seDeconnecter()

    ## Propriete : prenom du Client
    @property
    def prenom(self):
        return self.__prenom

    ## Propriete : nom du Client
    @property
    def nom(self):
        return self.__nom

    ## Propriete : id du Client
    @property
    def id(self):
        return self.__id

    ## Propriete : cb du Client
    @property
    def cb(self):
        return self.__cb

    ## Propriete : abonnement du Client
    @property
    def abonnement(self):
        return self.__typeAbonnement

    ## Retourne le nombre de super abonné
    # @return nombre de super abonné
    @staticmethod
    def nbSuperAbo():
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM client WHERE typeAbonnement = " + str(TypeAbonnement.SUPER_ABONNE))
        nb = r.fetchone()[0]
        c.seDeconnecter()
        return nb

    ## Retourne le nombre d'abonné
    # @return nombre d'abonné
    @staticmethod
    def nbAbo():
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM client WHERE typeAbonnement = " + str(TypeAbonnement.ABONNE))
        nb = r.fetchone()[0]
        c.seDeconnecter()
        return nb



    ## Representation du Client en chaine
    def __str__(self):
        return "[Client :" \
               " id = " + str(self.__id) + ", "+\
               " prenom = " + str(self.__prenom) + ", "+\
               " nom = " + str(self.__nom) + ", " +\
               " cb = " + str( self.__cb) + ", " +\
               " typeAbonnement = " + str(self.__typeAbonnement) + "]"

## Classe définissant les constantes de TypeAbonnement disponible pour le Client
class TypeAbonnement:
    ABONNE = 0
    SUPER_ABONNE = 1



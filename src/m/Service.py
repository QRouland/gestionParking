import time

from src.c.utils.connexionBDD import connexionBDD
from src.m.Abonnement import Client
from src.m.Parking import Placement


## Representation d'un Service de DreamPack
class Service:
    ## Retourne tout les services en cours dans le Parking parking
    # @param parking Parking dont on veut connaitre les services
    # @return Liste Service en cours
    @staticmethod
    def getAllEnCours(parking):
        c = connexionBDD()
        r = c.execute("SELECT idService FROM service WHERE dateRealisation is NULL "
                      "AND idPlacement IN (SELECT idPlacement FROM PLACEMENT WHERE "
                      "idPlace IN (SELECT idPlace FROM Place WHERE idParking = '" + str(parking.id) + "'))")
        rows = r.fetchall()
        c.seDeconnecter()
        l = []
        for row in rows:
            l.append(Service(row["idService"]))
        print("l = " + str(l))
        return l

    ## Retourne tout les services associé a un Placement
    # @param parking Parking dont on veut connaitre les services
    # @return Liste Service associé a un Placement
    @staticmethod
    def getAllServicePlacement(placement):
        c = connexionBDD()
        r = c.execute("SELECT idService FROM service WHERE idPlacement ='" + str(placement.id) + "'")
        rows = r.fetchall()
        c.seDeconnecter()
        l = []
        for row in rows:
            l.append(Service(row["idService"]))
        print("l = " + str(l))
        return l

    ## Contructeur d'un Service
    # @param id Si None : Cree un Service dans la BD Sinon : tentative de récupération du Service avec cet id dans la bd
    # @param client Si creation : Client associe au Service
    # @param placement Si creation : Placement associe au Service
    # @param typeService Si creation : TypeService du Service
    # @param dateService Si creation : date ou sera realise le service si necessaire
    # @param lieu Si creation : lieu ou realise le service si necessaire
    def __init__(self, id, client=None, placement=None, typeService=None,
                 dateService="NULL", lieu =""):
        if id is None:
            self.__client = client
            self.__placement = placement
            self.__typeService = typeService
            self.__dateDemande = time.time()
            self.__dateService = dateService
            self.__dateRealisation = "NULL"
            self.__lieu = lieu
            c = connexionBDD()
            c.execute("INSERT INTO service (idClient,idPlacement, typeService, dateDemande,dateService,lieu) VALUES (?,?,?,?,?,?)",
                      (str(self.__client.id), str(self.__placement.id), str(self.__typeService),
                       str(self.__dateDemande), str(self.__dateService),str(self.__lieu)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM service WHERE idService='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__id = id
            self.__client = Client(row["idClient"])
            self.__placement = Placement(row["idPlacement"])
            self.__typeService = row["typeService"]
            self.__dateDemande = row["dateDemande"]
            self.__dateService = row["dateService"]
            self.__dateRealisation = row["dateRealisation"]
            self.__lieu = row["lieu"]

    ## Propriete : id Service
    @property
    def id(self):
        return self.__id

    ## Propriete : TypeService du Service
    @property
    def typeService(self):
        return self.__typeService

    ## Propriete : Placement associe au Service
    @property
    def placement(self):
        return self.__placement

    ## Propriete : date ou le Service doit etre realisé
    @property
    def dateService(self):
        return self.__dateService

    ## Propriete : lieu ou le Service doit etre realisé
    @property
    def lieu(self):
        return self.__lieu

    ## Propriete : information interessante pout l'admin pour un Service
    @property
    def info(self):
        return "Place : " + self.__placement.place.identification + " Imma : " + self.__placement.voiture.immatriculation

    ## Propriete : Retour si un service a été réalisé du Service
    @property
    def estRealise(self):
        return self.__dateRealisation is not None and not self.__dateRealisation == "NULL"

    ## Passe le service comme realise
    def doService(self):
        self.__dateRealisation = time.time()
        c = connexionBDD()
        c.execute("UPDATE service SET dateRealisation = '" + str(self.__dateRealisation) + "' WHERE idService='" + str(
            self.__id) + "'")
        c.seDeconnecter()

    ## Passe a un service a un etat de non realisé si le Client recupere sa Voiture avant que le Service est été réalisé
    def nonRealise(self):
        self.__dateRealisation = 1
        c = connexionBDD()
        c.execute("UPDATE service SET dateRealisation = '" + str(self.__dateRealisation) + "' WHERE idService='" + str(
            self.__id) + "'")
        c.seDeconnecter()

    ## mise a jour de infos de livraison
    def maj(self, datetime, lieu):
        self.__dateService = datetime
        self.__lieu = lieu
        c = connexionBDD()
        c.execute("UPDATE service SET dateService = '" + str(self.__dateService) +
                  "' , lieu = '" + str(self.__lieu) +
                  "' WHERE idService='" + str(self.__id) + "'")
        c.seDeconnecter()

    ## Representation en chaine d'un Service
    def __str__(self):
        return "[Service : " \
               "id = " + str(self.__id) + ","+\
               "Client = " + str(self.__client) + "," +\
               "Placement = " + str(self.__placement) + "," +\
               "TypeService = " + str( self.__typeService) + ","+\
               "DateDemande = " + str(self.__dateDemande) + ","+\
               "DateService = " + str( self.__dateService) + "," +\
               "DateRealisation = " + str(self.__dateRealisation) + \
               "Lieu = " + str( self.__lieu) +" ]"

## Classe Representant les différents TypeService
class TypeService:
    MAINTENANCE = 1
    ENTRETIEN = 2
    LIVRAISON = 3
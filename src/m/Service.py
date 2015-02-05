import time

from src.m.Client import Client
from src.m.Parking import Placement
from src.m.connexionBDD import connexionBDD


__author__ = 'sidya'


class Service:
    @staticmethod
    def getAllEnCours(parking):
        c = connexionBDD()
        r = c.execute("SELECT * FROM service WHERE dateRealisation is NULL "
                      "AND idPlacement IN (SELECT idPlacement FROM PLACEMENT WHERE "
                      "idPlace IN (SELECT idPlace FROM Place WHERE idParking = '" + str(parking.id) + "'))")
        rows = r.fetchall()
        c.seDeconnecter()
        l = []
        for row in rows:
            l.append(Service(row["idService"], Client(row["idClient"]), Placement(row["idPlacement"]),
                             row["typeService"], row["dateDemande"], row["dateService"], row["dateRealisation"]))
        print("l = " + str(l))
        return l

    @staticmethod
    def getAllServicePlacement(placement):
        c = connexionBDD()
        r = c.execute("SELECT * FROM service WHERE idPlacement ='" + str(placement.id) + "'")
        rows = r.fetchall()
        c.seDeconnecter()
        l = []
        for row in rows:
            l.append(Service(row["idService"], Client(row["idClient"]), Placement(row["idPlacement"]),
                             row["typeService"], row["dateDemande"], row["dateService"], row["dateRealisation"]))
        print("l = " + str(l))
        return l

    def __init__(self, id, client=None, placement=None, typeService=None,
                 dateService=None, dateDemande=time.time(), dateRealisation=None):
        if id is None:
            self.__client = client
            self.__placement = placement
            self.__typeService = typeService
            self.__dateDemande = dateDemande
            self.__dateService = dateService
            self.__dateRealisation = dateRealisation
            c = connexionBDD()
            c.execute("INSERT INTO service (idClient,idPlacement, typeService, dateDemande) VALUES (?,?,?,?)",
                      (str(self.__client.id), str(self.__placement.id), str(self.__typeService),
                       str(self.__dateDemande)))
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


    @property
    def id(self):
        return self.__id

    @property
    def typeService(self):
        return self.__typeService

    @property
    def placement(self):
        return self.__placement

    @property
    def info(self):
        str = "Place : " + self.__placement.place.identification + "Imma : " + self.__placement.voiture.immatriculation
        if self.typeService == TypeService.LIVRAISON:
            str += "Date : " + self.__dateService
        return str

    @property
    def estRealise(self):
        return self.__dateRealisation is None or self.__dateRealisation == "NULL"

    def doService(self):
        self.__dateRealisation = time.time()
        c = connexionBDD()
        c.execute("UPDATE service SET dateRealisation = '" + str(self.__dateRealisation) + "' WHERE idService='" + str(
            self.__id) + "'")
        c.seDeconnecter()

    def __str__(self):
        return "[Service : " \
               "id = " + str(self.__id) + "," \
                                          "Client = " + str(self.__client) + "," \
                                                                             "TypeService = " + str(
            self.__typeService) + "," \
                                  "DateDemande = " + str(self.__dateDemande) + "," \
                                                                               "DateService = " + str(
            self.__dateService) + "," \
                                  "DateRealisation = " + str(self.__dateRealisation) + "]"


class TypeService:
    MAINTENANCE = 1
    ENTRETIEN = 2
    LIVRAISON = 3
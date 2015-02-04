import random
import string
import time
from src.m.Voiture import Voiture
from src.m.connexionBDD import connexionBDD

__author__ = 'sidya'



class Parking:
    parkings = []
    @staticmethod
    def get(id):
        if len(Parking.parkings) == 0 :
            Parking.getAllActif()
        for p in Parking.parkings :
            if p.id == id :
                return p

    @staticmethod
    def getAllActif():
        if len(Parking.parkings) == 0 :
            c = connexionBDD()
            r = c.execute("SELECT * FROM parking WHERE actif = 1")
            rows = r.fetchall()
            c.seDeconnecter()
            for row in rows :
                Parking(row["idParking"], row["nom"], None)
        return Parking.parkings

    @staticmethod
    def remove(parking):
        Parking.parkings.remove(parking)
        c = connexionBDD()
        c.execute("UPDATE parking SET actif = 0 WHERE idParking='"+str(parking.id)+"'")
        c.seDeconnecter()

    @staticmethod
    def removeAllRam():
        Parking.parkings = []


    def __init__(self, id, nom=None, listeTypePlace=None):
        self.__nom = nom
        if id is None :
            c = connexionBDD()
            c.execute("INSERT INTO parking (nom) VALUES ('"+str(self.__nom)+"')", ())
            self.__id = c.lastId()
            #Crea des places
            n = 0
            for typePlace in listeTypePlace :
                for i in range(typePlace.nombre) :
                    print(Place(None,self,typePlace,n,1,True,False))
                    n += 1
        else :
            self.__id = id
        self.parkings.append(self)

    @property
    def id(self):
        return self.__id

    @property
    def nom(self):
        return self.__nom

    @property
    def nbPlaces(self):
        return Place.nbPlaceParking(self.__id)

    @property
    def nbPlacesLibresParking(self):
        return Place.nbPlaceLibreParking(self.__id)

    @property
    def nbSuperAbo(self):
        return Place.nbSuperAbo(self.__id)

    def recherchePlace(self, voiture):
        """
        Permet de rechercher une place valide pour une voiture
        :param voiture: Voiture
        :return: Place
        """
        return Place.placeValide(self.__id, voiture)

    def addPlaceSuperAbo(self, parking):
        return Place(None, parking, None, None, None, True)

    def __str__(self):
        return "[Parking : nom = " + self.__nom +"]"


class Place:
    def __init__(self, id=None, parking=None, typePlace=None, numero=None, niveau=None,estLibre=True, estSuperAbo=False):
        if id is None :
            self.__parking = parking
            self.__typePlace = typePlace
            self.__numero = numero
            self.__niveau = niveau
            self.__estLibre = estLibre
            self.__estSuperAbo = estSuperAbo
            c = connexionBDD()
            c.execute("INSERT INTO place (idParking, idTypePlace, numero, estLibre, estSuperAbo) "
                      "VALUES (?,?,?,?,?)",
                      (self.__parking.id, self.__typePlace.id,
                       self.__numero, int(self.__estLibre), int(self.__estSuperAbo)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else :
            c = connexionBDD()
            r = c.execute("SELECT * FROM place WHERE idPlace='"+str(id)+"'")
            row = r.fetchone()
            if row is None :
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__parking = Parking.get(row["idParking"])
            self.__typePlace = TypePlace(row["idTypePlace"])
            self.__numero =  row["numero"]
            self.__estLibre = row["estLibre"]
            self.__estSuperAbo = row["estSuperAbo"]
            self.__id = id

    @property
    def id(self):
        return self.__id

    def prendre(self):
        """
        Rend la place indisponible
        :param Placement:
        :return:
        """
        if (self.__estLibre == False):
            raise Exception("Place déjà prise")
        self.__estLibre = False
        c = connexionBDD()
        c.execute("UPDATE place SET estLibre = 0 WHERE idPlace ='"+str(self.__id)+"'")
        c.seDeconnecter()

    def liberer(self):
        """
        Libere une place non dispo
        :return:
        """
        if (self.__estLibre == True):
            raise Exception("Impossible de liberer une place vide")
        self.__estLibre = True
        c = connexionBDD()
        c.execute("UPDATE place SET estLibre = 1 WHERE idPlace ='"+str(self.__id)+"'")
        c.seDeconnecter()

    @property
    def identification(self):
        return TypePlace(self.__typePlace).niveau + ":" + self.__numero

    @property
    def estlibre(self):
        return self.__estLibre

    @staticmethod
    def nbPlaceParking(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = " + str(idParking))
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    @staticmethod
    def nbPlaceLibreParking(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = "+str(idParking)+" AND estLibre = 1")
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    @staticmethod
    def nbSuperAbo(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = "+str(idParking)+" AND estSuperAbo = 1")
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    @staticmethod
    def placeValide(idPArking, voiture):
        c = connexionBDD()
        r = c.execute("SELECT * FROM place WHERE idParking= ? AND estLibre = 1 "
                      "AND idTypePlace =(SELECT idTypePlace FROM typePlace "
                      "WHERE hauteur>? AND longueur>? ORDER BY longueur) ",
                    (str(idPArking),str(voiture.hauteur),str(voiture.longueur)))
        row = r.fetchone()
        c.seDeconnecter()
        if row is None :
            return None
        else :
            return Place(row["idPlace"],row["idParking"], row["idTypePlace"],
                         row["numero"], bool(row["estLibre"]), bool(row["estSuperAbo"]))


    def __str__(self):
        return "[Place : " \
               "Parking = " + str(self.__parking) + "," \
               "typePlace = " + str(self.__typePlace) + "," \
               "numero = " + str(self.__numero) + "," \
               "estLibre = " + str(self.__estLibre) + "," \
               "estSuperAbo = " + str(self.__estSuperAbo) + "]" \





class TypePlace:
    def __init__(self, id ,longueur=None, hauteur=None, nombre=None, prix=None, niveau=None):
        if id is None :
            self.__longueur = longueur
            self.__hauteur = hauteur
            self.__nombre = nombre
            self.__prix = prix
            self.__niveau = niveau
            c = connexionBDD()
            c.execute("INSERT INTO typePlace (longueur,hauteur,nombre, prix, niveau) VALUES (?,?,?,?,?)",
                      (self.__longueur, self.__hauteur, self.__nombre,self.__prix, self.__niveau))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM typePlace WHERE idTypePlace='"+str(id)+"'")
            row = r.fetchone()
            if row is None :
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__longueur = row["longueur"]
            self.__hauteur = row["hauteur"]
            self.__nombre = row["nombre"]
            self.__prix = row["prix"]
            self.__niveau = row["niveau"]
            self.__id = id

    @property
    def id(self):
        return self.__id

    @property
    def longueur(self):
        return self.__longueur

    @property
    def hauteur(self):
        return self.__hauteur

    @property
    def nombre(self):
        return self.__nombre

    @property
    def prix(self):
        return self.__prix

    @property
    def niveau(self):
        return self.__niveau

    def __str__(self):
        return "[TypePlace : " \
               "id = " + str(self.__id) + "," \
               "longueur = " + str(self.__longueur) + "," \
               "hauteur = " + str(self.__hauteur) + "," \
               "nombre = " + str(self.__nombre) + "," \
               "prix = " + str(self.__prix) + "," \
               "niveau = " + str(self.__niveau) + "]"


class Placement:
    def __init__(self, id, voiture=None, place=None, debut=None, fin=None):
        """
        Creer un placement
        :param voiture: Voiture
        :param place: Place
        :return:
        """
        if id is None :
            self.__voiture = voiture
            self.__place = place
            self.__debut = time.time()
            self.__fin = None
            while True:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                         range(random.randint(1, 10)))
                try:
                    Placement.get(id)
                except IndexError:
                    break
            c = connexionBDD()
            c.execute("INSERT INTO placement (idPlacement,idVoiture,idPlace, debut, fin) VALUES (?,?,?,?,?)",
                      (str(id), str(self.__voiture.id), str(self.__place.id), str(self.__debut), "NULL"))
            self.__id = id
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM placement WHERE idPlacement='"+str(id)+"'")
            row = r.fetchone()
            if row is None :
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__voiture = row["voiture"]
            self.__place = row["place"]
            self.__id = id
            self.__debut = debut
            self.__fin = fin

    @property
    def id(self):
        return self.__id

    @property
    def place(self):
        return self.__place

    def end(self):
        self.__fin = time.time()
        c = connexionBDD()
        c.execute("UPDATE placement SET fin='"+str(self.__fin)+"' WHERE idPlacement='"+str(id)+"'")
        c.seDeconnecter()

    def __str__(self):
        return "[Placement : " \
               "id = " + str(self.__id) +"," \
               "Voiture = " + str(self.__voiture) +"," \
               "Place = " + str(self.__place) +"," \
               "Debut = " + str(self.__debut) +"," \
               "Fin = " + str(self.__fin) +"]"
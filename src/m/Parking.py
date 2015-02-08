"""
    Module qui implémente les classes representants un parking de DreamPark.
"""
import random
import string
import time
from datetime import datetime

from src.c.utils.connexionBDD import connexionBDD
from src.m.Voiture import Voiture



## Representation d'un parking de DreamPark
class Parking:
    parkings = []

    ## Retourne un objet parking correspondant à id
    # @param id id du Parking a retourner
    @staticmethod
    def get(id):
        if len(Parking.parkings) == 0:
            Parking.getAllActif()
        for p in Parking.parkings:
            if p.id == id:
                return p

    ## Retourne tout les Parking actif present dans la bd
    @staticmethod
    def getAllActif():
        if len(Parking.parkings) == 0:
            c = connexionBDD()
            r = c.execute("SELECT * FROM parking WHERE actif = 1")
            rows = r.fetchall()
            c.seDeconnecter()
            for row in rows:
                Parking(row["idParking"], row["nom"], None)
        return Parking.parkings

    ## Supprime un parking
    # @param parking L'objet parking a supprimer
    @staticmethod
    def remove(parking):
        Parking.parkings.remove(parking)
        c = connexionBDD()
        c.execute("UPDATE parking SET actif = 0 WHERE idParking='" + str(parking.id) + "'")
        c.seDeconnecter()

    ## Supprime les parkings present dans la mémoire vive (pas dans la bd)
    @staticmethod
    def removeAllRam():
        Parking.parkings = []

    ## Constructeur du Parking
    # @param id Si None : Cree un Parking dans la BD Sinon : tentative de récupération du Parking avec cet id dans la bd
    # @param nom : Si creation nom du parking
    # @param listeTypePlace : Si creation Liste des TypePlace du parking
    def __init__(self, id, nom=None, listeTypePlace=None):
        self.__nom = nom
        if id is None:
            c = connexionBDD()
            c.execute("INSERT INTO parking (nom) VALUES ('" + str(self.__nom) + "')", ())
            self.__id = c.lastId()
            # Crea des places
            n = 0
            placeParNiveau = {}
            for typePlace in listeTypePlace:
                try:
                    i = placeParNiveau[typePlace.niveau]
                except KeyError:
                    i = 0
                placeParNiveau[typePlace.niveau] = i + typePlace.nombre
                for i in range(placeParNiveau[typePlace.niveau]):
                    Place(None, self, typePlace, i, True, False)
        else:
            self.__id = id
        self.parkings.append(self)

    ## Propriete : id du Parking
    @property
    def id(self):
        return self.__id

    ## propriete : nom du Parking
    @property
    def nom(self):
        return self.__nom

    ## propriete : nombre de Place du Parking
    @property
    def nbPlaces(self):
        return Place.nbPlaceParking(self.__id)

    ## propriete : nombre de Place libres du Parking
    @property
    def nbPlacesLibresParking(self):
        return Place.nbPlaceLibreParking(self.__id)

    ## propriete : nombre de Place super abo
    @property
    def nbSuperAbo(self):
        return Place.nbSuperAbo(self.__id)

    ## propriete : listeTypePlace
    @property
    def listeTypePlace(self):
        c = connexionBDD()
        r = c.execute("SELECT idTypePlace FROM typePlace WHERE idTypePlace in (SELECT idTypePlace FROM place WHERE idParking = '" + str(self.__id) + "')")
        rows = r.fetchall()
        c.seDeconnecter()
        l = []
        for row in rows:
            l.append(TypePlace(row["idTypePlace"]))
        return l

    ## Recherche une place pour une voiture
    # @param voiture voiture pour laquel on recherche la place
    # @return Place Si touvé : Place sinon : None
    def recherchePlace(self, voiture):
        return Place.placeValide(self.__id, voiture)

    ## Ajout d'une place surmesure pour super abo
    # @param parking le parking ou il faut ajouter la place
    def addPlaceSuperAbo(self):
        return Place(None, self, None, None, False, True)

    ## Representation du Parking en chaine
    def __str__(self):
        return "[Parking : nom = " + self.__nom + "]"

## Representation d'une place de DreamPark
class Place:
    ## Contructeur de Place
    # @param id Si None : creation de la Place dans la bd Sinon : tentative de récupération de la Place avec cet id dans la bd
    # @param parking Si creation : le Parking ou est creer la Place
    # @param typePlace Si creation : le TypePlace de Place
    # @param numero Si creation : le numero de Place
    # @param estLibre Si creation : Si la Place est libre ou non
    # @param estSuperAbo Si creation : Si la Place est superAbo ou non
    def __init__(self, id, parking=None, typePlace=None, numero=None, estLibre=True, estSuperAbo=False):
        if id is None:
            self.__parking = parking
            self.__typePlace = typePlace
            self.__numero = numero
            self.__estLibre = estLibre
            self.__estSuperAbo = estSuperAbo
            if self.__typePlace is None:
                t = "NULL"
            else:
                t = self.__typePlace.id
            c = connexionBDD()
            c.execute("INSERT INTO place (idParking, idTypePlace, numero, estLibre, estSuperAbo) "
                      "VALUES (?,?,?,?,?)",
                      (self.__parking.id, t,
                       self.__numero, int(self.__estLibre), int(self.__estSuperAbo)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM place WHERE idPlace='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__parking = Parking.get(row["idParking"])
            self.__typePlace = TypePlace(row["idTypePlace"])
            self.__numero = row["numero"]
            self.__estLibre = row["estLibre"]
            self.__estSuperAbo = row["estSuperAbo"]
            self.__id = id



    ## Rend la Place la indisponible
    def prendre(self):
        if (self.__estLibre == False):
            raise Exception("Place déjà prise")
        self.__estLibre = False
        c = connexionBDD()
        c.execute("UPDATE place SET estLibre = 0 WHERE idPlace ='" + str(self.__id) + "'")
        c.seDeconnecter()

    ## Rend la Place disponible
    def liberer(self):
        if (self.__estLibre == True):
            raise Exception("Impossible de liberer une place vide")
        self.__estLibre = True
        c = connexionBDD()
        c.execute("UPDATE place SET estLibre = 1 WHERE idPlace ='" + str(self.__id) + "'")
        c.seDeconnecter()

    ## Suppression place de la bd
    def supprimer(self):
        c = connexionBDD()
        c.execute("DELETE FROM place idPlace ='" + str(self.__id) + "'")
        c.seDeconnecter()

    ## propriete : id de la Place
    @property
    def id(self):
        return self.__id

    ## propriete : identification etage : numero de la Place
    @property
    def identification(self):
        return str(chr(self.__typePlace.niveau + ord('A')) + ":" + str(self.__numero))

    ## propriete : True si la place est Place
    @property
    def estlibre(self):
        return self.__estLibre

    ## propriete : typePlace de la Place
    @property
    def typePlace(self):
        return self.__typePlace

    ## propriete : typePlace de la Place
    @property
    def estSuperAbo(self):
        return self.__estSuperAbo

    ## Retourne les nombre de place du Parking d'id idParking
    # @param idParking l'id du Parking
    # @return le nombre de Place
    @staticmethod
    def nbPlaceParking(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = " + str(idParking))
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    ## Retourne les nombre de place libre du Parking d'id idParking
    # @param idParking l'id du Parking
    # @return le nombre de Place libre
    @staticmethod
    def nbPlaceLibreParking(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = " + str(idParking) + " AND estLibre = 1")
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    ## Retourne les nombre de place superAbo du Parking d'id idParking
    # @param idParking l'id du Parking
    # @return le nombre de Place superAbo
    @staticmethod
    def nbSuperAbo(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = " + str(idParking) + " AND estSuperAbo = 1")
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    ## Retourne si une Place valide pour une Voiture dans un parking
    # @param idParking id du Parking ou est recherché la place
    # @param voiture Voiture pour laquelle est recherché la place
    # @return Si non trouve : None. Sinon : Place une place valide
    @staticmethod
    def placeValide(idPArking, voiture):
        c = connexionBDD()
        r = c.execute("SELECT * FROM place WHERE idParking= ? AND estLibre = 1 "
                      "AND idTypePlace =(SELECT idTypePlace FROM typePlace "
                      "WHERE hauteur>? AND longueur>? ORDER BY longueur) ",
                      (str(idPArking), str(voiture.hauteur), str(voiture.longueur)))
        row = r.fetchone()
        c.seDeconnecter()
        if row is None:
            return None
        else:
            return Place(row["idPlace"], row["idParking"], row["idTypePlace"],
                         row["numero"], bool(row["estLibre"]), bool(row["estSuperAbo"]))


    ## Representation d'une Place en chaine
    def __str__(self):
        return "[Place : " +\
               "Parking = " + str(self.__parking) + ","+\
               "typePlace = " + str(self.__typePlace) + ","+\
               "numero = " + str(self.__numero) + ","+\
               "estLibre = " + str(self.__estLibre) + ","+\
               "estSuperAbo = " + str(self.__estSuperAbo) + "]"


## Representation d'un TypePlace de DreamPark
class TypePlace:
    ## Constructeur de TypePlace
    # @param id Si None : creation du TypePlace dans la bd Sinon : tentative de récupération du TypePlace avec cet id dans la bd
    # @param longueur Longueur de la Place en cm
    # @param hauteur Hauteur de la Place en cm
    # @param nombre Nombre de Place de ce type
    # @param prix Le prix pur ce type de Place
    # @param niveau Le niveau ou se trouve les Place
    def __init__(self, id, longueur=None, hauteur=None, nombre=None, prix=None, niveau=None):
        if id is None:
            self.__longueur = longueur
            self.__hauteur = hauteur
            self.__nombre = nombre
            self.__prix = prix
            self.__niveau = niveau
            c = connexionBDD()
            c.execute("INSERT INTO typePlace (longueur,hauteur,nombre, prix, niveau) VALUES (?,?,?,?,?)",
                      (self.__longueur, self.__hauteur, self.__nombre, self.__prix, self.__niveau))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM typePlace WHERE idTypePlace='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__longueur = row["longueur"]
            self.__hauteur = row["hauteur"]
            self.__nombre = row["nombre"]
            self.__prix = row["prix"]
            self.__niveau = row["niveau"]
            self.__id = id

    ## propriete : id du Typeplace
    @property
    def id(self):
        return self.__id

    ## propriete : longueur du Typeplace
    @property
    def longueur(self):
        return self.__longueur

    ## propriete : hauteur du Typeplace
    @property
    def hauteur(self):
        return self.__hauteur

    ## propriete : nombre du Typeplace
    @property
    def nombre(self):
        return self.__nombre

    ## propriete : prix du Typeplace
    @property
    def prix(self):
        return self.__prix

    ## propriete : niveau du Typeplace
    @property
    def niveau(self):
        return self.__niveau

    ## Representation du TypePlace en chaine
    def __str__(self):
        return "[TypePlace : " \
               "id = " + str(self.__id) + ","+\
               "longueur = " + str(self.__longueur) + ","+\
               "hauteur = " + str(self.__hauteur) + ","+\
               "nombre = " + str(self.__nombre) + "," +\
               "prix = " + str(self.__prix) + ","+\
               "niveau = " + str(self.__niveau) + "]"

## Representation d'un Placement de DreamPark
class Placement:
    ## Constructeur Placement
    # @param id Si None : creation du Placement dans la bd Sinon : tentative de récupération du Placement avec cet id dans la bd
    # @param voiture Si creation : Voiture lié au Placement
    # @param place Si creation : Place  lié au Placement
    def __init__(self, id, voiture=None, place=None):
        if id is None:
            self.__voiture = voiture
            self.__place = place
            self.__debut = time.time()
            self.__fin = None
            while True:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                             range(random.randint(1, 10)))
                try:
                    Placement(id)
                except IndexError:
                    break
            c = connexionBDD()
            c.execute("INSERT INTO placement (idPlacement,idVoiture,idPlace, debut, fin) VALUES (?,?,?,?,?)",
                      (str(id), str(self.__voiture.id), str(self.__place.id), str(self.__debut), "NULL"))
            self.__id = id
            c.seDeconnecter()
        else:
            c = connexionBDD()
            r = c.execute("SELECT * FROM placement WHERE idPlacement='" + str(id) + "'")
            row = r.fetchone()
            if row is None:
                raise IndexError("Invalid id")
            c.seDeconnecter()
            self.__voiture = Voiture(row["idVoiture"])
            self.__place = Place(row["idPlace"])
            self.__id = id
            self.__debut = row["debut"]
            self.__fin = row["fin"]

    ## Propriete : id du Placement
    @property
    def id(self):
        return self.__id

    ## Propriete : place liée du Placement
    @property
    def place(self):
        return self.__place

    ## Propriete : voiture liée du Placement
    @property
    def voiture(self):
        return self.__voiture

    ## Retourne la durée moyenne des placement
    # @return duree moyenne placement
    @staticmethod
    def dureeMoyPlacement():
        c = connexionBDD()
        r= c.execute("SELECT AVG(FIN - DEBUT) AS duree FROM placement")
        nb = r.fetchone()[0]
        c.seDeconnecter()
        return nb

    ## Fin du placement (depart voiture)
    def end(self):
        self.__fin = time.time()
        c = connexionBDD()
        c.execute("UPDATE placement SET fin='" + str(self.__fin) + "' WHERE idPlacement='" + str(self.__id) + "'")
        c.seDeconnecter()
        self.__place.liberer()

    ## Representation du Placement en chaine
    def __str__(self):
        return "[Placement : " \
               "id = " + str(self.__id) + "," +\
               "Voiture = " + str(self.__voiture) + ","+\
               "Place = " + str(self.__place) + "," +\
               "Debut = " + str( self.__debut) + "," +\
               "Fin = " + str(self.__fin) + "]"
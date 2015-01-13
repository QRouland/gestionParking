import random
import string
import datetime
from src.m.Voiture import Voiture
from src.m.connexionBDD import connexionBDD

__author__ = 'sidya'



class Parking:
    parkings = []

    @staticmethod
    def get(id):
        for p in Parking.parkings :
            if p.id == id :
                return p

    @staticmethod
    def getAll():
        return Parking.parkings


    def __init__(self, nom, listeTypePlace):
        self.__nom = nom
        c = connexionBDD()
        c.execute("INSERT INTO parking (nom) VALUES ('"+str(self.__nom)+"')", ())
        self.__id = c.lastId()

        #Crea des places
        n = 0
        for typePlace in listeTypePlace :
            for i in range(typePlace.nombre) :
                print(Place(None,self,typePlace,1,n,True,False))
                n += 1
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

    def __str__(self):
        return "[Parking : nom = " + self.__nom +"]"


class Place:
    @staticmethod
    def get(id):
        c = connexionBDD()
        r = c.execute("SELECT * FROM place WHERE idPlace='"+str(id)+"'")
        row = r.fetchone()
        if row is None :
            raise IndexError("Invalid id")
        c.seDeconnecter()
        return Place(id,row["idParking"],row["idTypePlace"],row["niveau"],
                     row["numero"],row["estLibre"],row["estSuperAbo"])

    def __init__(self, id, parking, typePlace, niveau, numero, estLibre, estSuperAbo):
        self.__parking = parking
        self.__typePlace = typePlace
        self.__niveau = niveau
        self.__numero = numero
        self.__estLibre = estLibre
        self.__estSuperAbo = estSuperAbo
        if id is None :
            c = connexionBDD()
            c.execute("INSERT INTO place (idParking, idTypePlace, niveau, numero, estLibre, estSuperAbo) "
                      "VALUES (?,?,?,?,?,?)",
                      (self.__parking.id, self.__typePlace.id,self.__niveau,
                       self.__numero, self.__estLibre, int(self.__estSuperAbo)))
            self.__id = c.lastId()
            c.seDeconnecter()
        else :
            self.__id = id

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
        c.execute("UPDATE place SET estLibre = 0 WHERE idPlace = ?", (str(self.__id)))
        c.seDeconnecter()

    def liberer(self):
        """
        Libere une place non dispo
        :return:
        """
        if (self.__estLibre == True):
            raise Exception("Impossible de liberer une place vide")
        self.__estLibre = False
        c = connexionBDD()
        c.execute("UPDATE place SET estLibre = 1 WHERE idPlace = ?", (str(self.__id)))
        c.seDeconnecter()

    @staticmethod
    def nbPlaceParking(idParking):
        c = connexionBDD()
        print("lol")
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = ?", (str(idParking)))
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    @staticmethod
    def nbPlaceLibreParking(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = ? AND estLibre = 1", (str(idParking)))
        row = r.fetchone()
        c.seDeconnecter()
        return row[0]

    @staticmethod
    def nbSuperAbo(idParking):
        c = connexionBDD()
        r = c.execute("SELECT COUNT(*) FROM place WHERE idParking = ? AND estSuperAbo = 1", (str(idParking)))
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
            return Place(row["idPlace"],row["idParking"], row["idtypePlace"],
                         row["niveau"], row["numero"], bool(row["estLibre"]), bool(row["estSuperAbo"]))


    def __str__(self):
        return "[Place : " \
               "Parking = " + str(self.__parking) + "," \
               "typePlace = " + str(self.__typePlace) + "," \
               "niveau = " + str(self.__niveau) + "," \
               "numero = " + str(self.__numero) + "," \
               "estLibre = " + str(self.__estLibre) + "," \
               "estSuperAbo = " + str(self.__estSuperAbo) + "]" \

    @property
    def id(self):
        return self.__id



class TypePlace:
    @staticmethod
    def get(id):
        c = connexionBDD()
        r = c.execute("SELECT * FROM typePlace WHERE idTypePlace='"+str(id)+"'")
        row = r.fetchone()
        if row is None :
            raise IndexError("Invalid id")
        c.seDeconnecter()
        return TypePlace(id,row["longueur"],row["hauteur"],row["nombre"])


    def __init__(self, id ,longueur, hauteur, nombre):
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__nombre = nombre
        if id is None :
            c = connexionBDD()
            c.execute("INSERT INTO typePlace (longueur,hauteur,nombre) VALUES (?,?,?)",
                      (self.__longueur, self.__hauteur, self.__nombre))
            self.__id = c.lastId()
            c.seDeconnecter()
        else:
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

    def __str__(self):
        return "[TypePlace : " \
               "id = " + str(self.__id) + "," \
               "longueur = " + str(self.__longueur) + "," \
               "hauteur = " + str(self.hauteur) + "," \
               "nombre = " + str(self.nombre) + "]"


class Placement:
    placementsEnCours = []

    @staticmethod
    def get(id):
        c = connexionBDD()
        r = c.execute("SELECT * FROM placement WHERE idPlacement='"+str(id)+"'")
        row = r.fetchone()
        if row is None :
            raise IndexError("Invalid id")
        c.seDeconnecter()
        print(row["idVoiture"])
        return Placement(row["idPlacement"], Voiture.get(row["idVoiture"]), Place.get(row["idPlace"]),
                         row["debut"], row["fin"])


    def __init__(self,id, voiture, place, debut, fin):
        """
        Creer un placement
        :param voiture: Voiture
        :param place: Place
        :return:
        """
        self.__voiture = voiture
        self.__place = place
        place.prendre()
        self.placementsEnCours.append(self)
        if id is None :
            self.__debut = datetime.datetime
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
            self.__id = id
            self.__debut = debut
            self.__fin = fin

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return "[Placement : " \
               "id = " + self.__id +"," \
               "Voiture = " + self.__voiture +"," \
               "Place = " + self.__place +"," \
               "Debut = " + self.__debut +"," \
               "Fin = " + self.__fin +"]"




if __name__ == "__main__" :
    c = connexionBDD()
    c.initialisationBDD()
    c.seDeconnecter()
    listeTypePlaces = []
    listeTypePlaces.append(TypePlace(None,200, 300,10))
    listeTypePlaces.append(TypePlace(None,120, 250,15))
    p = Parking("test",listeTypePlaces)
    print (p)
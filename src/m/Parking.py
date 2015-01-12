
from src.m.Place import Place

__author__ = 'sidya'

class Parking:
    """
        Definie un parking
    """
    def __init__(self, typePlaces, nom):
        """
        Creer objet parking
        :param typePlaces: ListeTypePlace
        :param nom: str
        :return:
        """
        self.__typePlaces = typePlaces
        self.__nom = nom
        self.__prix = 10
        self.__Places = {}
        l = []
        for t in typePlaces.liste:
            for i in range(0, t.nb):
                l.append(Place(i + 1, 1, t.longueur, t.hauteur))
        self.__Places = l


    @property
    def nom(self):
        return self.__nom

    @property
    def nbPlaces(self):
        return self.__typePlaces.nbPlaceTotal


    @property
    def nbPlacesLibresParking(self):
        i = 0
        for p in self.__Places:
            if p.estLibre:
                i += 1
        return i

    def recherchePlace(self, voiture):
        """
        Permet de rechercher une place valide pour une voiture
        :param voiture: Voiture
        :return: Place
        """
        place = None
        for p in self.__Places:
            if p.estLibre and p.dimValide(voiture.getHauteur, voiture.getLongueur) :
                pass
                place = p
                break
        return place


    def addAbonnement(self, Abonnement):
        pass

    def __str__(self):
        return "Parking :  niveau : " + str(self.__nbNiveaux)

__author__ = 'sidya'

from src.m.Place import Place, ListeTypePlace


class Parking:
    """
        Definie un parking
    """
    def __init__(self, nbNiv, typePlacesParNiv,nom):
        self.__nom = nom
        self.__nbPlacesParNiveau = typePlacesParNiv.nbPlaceTotal
        self.__prix = 10
        self.__nbNiveaux = nbNiv
        self.__Places = {}
        for n in range(0, nbNiv):
            l = []
            for t in typePlacesParNiv.liste:
                for i in range(0, t.nb):
                    l.append(Place(i + 1, n, t.longueur, t.hauteur))
            self.__Places[n ] = l

    def recherchePlace(self, voiture):
        place = None
        for i in range(0, self.__nbNiveaux):
            if place != None:
                break
            l = [p for p in self.__Places[i].estLibre]
            for p in l:
                if p.dimValide(voiture.hauteur, voiture.longueur):
                    pass
                    place = p
                    break
        return place

    def nbPlacesLibresNiveau(self, niveau):
        i = 0
        for p in self.__Places[niveau]:
            if p.estLibre:
                i += 1
        return i

    def nbPlacesLibresParking(self):
        nbP = 0
        for i in range(0,self.__nbNiveaux) :
            nbP += self.nbPlacesLibresNiveau(i)
        return nbP

    def addAbonnement(self, Abonnement):
        pass

    def __str__(self):
        return "Parking :  niveau : " + str(self.__nbNiveaux)


if __name__ == "__main__":
    l = ListeTypePlace()
    l.add(10, 11, 5)
    l.add(7, 12, 5)
    p = Parking(5, l)
    print(p)
    print(p.nbPlacesLibresNiveau(1))
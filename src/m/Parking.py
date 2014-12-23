__author__ = 'sidya'

from src.m.Place import Place, TypePlace, ListeTypePlace


class Parking:
    """
        Definie un parking
    """
    def __init__(self, nbNiv, typePlacesParNiv):
        #self.__nbPlacesParNiveau = placesParNiv
        self.__prix = 10
        self.__nbNiveaux = nbNiv
        self.__Places = {}
        for n in range(0, nbNiv):
            l = []
            for t in typePlacesParNiv.liste:
                for i in range(0, t.nb):
                    l.append(Place(i+1, n, t.longueur, t.hauteur))
            self.__Places[n+1] = l

    def recherchePlace(self, voiture):
        trouve = False
        for i in range(0, self.__nbNiveaux):
            if trouve :
                break
            l = [p for p in self.__Places[i].estLibre]
            for p in l :
                if p.dimValide(voiture.hauteur, voiture.longueur) :
                    pass
                    trouve = True
                    break
        return trouve

    def nbPlacesLibresNiveau(self, niveau):
        i = 0
        for p in self.__Places[niveau]:
            if p.estLibre:
                i += 1
        return i

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
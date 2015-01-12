

class Voiture():
    def __init__(self, longueur, hauteur, imma):
        self._hauteur = hauteur
        self._longueur = longueur
        self._immatriculation = imma
        self._estDansParking = False

    @property
    def getHauteur(self):
        return self._hauteur

    @property
    def getLongueur(self):
        return self._longueur

    @property
    def getImmatriculation(self):
        return self._immatriculation

    @property
    def estDansParking(self):
        return self._estDansParking == True

    #def addPlacement(self, placement):



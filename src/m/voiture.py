__author__ = 'nadiel'

class Voiture():
    def __init__(self):
        self._hauteur
        self._longueur
        self._immatriculation
        self._estDansParking

   # @hauteur.setter
    def setHauteur(self, value):
     self._hauteur=value

    @property
    def getHauteur(self):
        return self._hauteur

   # @longueur.setter
    def setLongueur(self, value):
            self._longueur=value

  # @immatriculation.setter
    def setImmatriculation(self, chaine):
        self._immatriculation = chaine

    @property
    def getImmatriculation(self):
        return self._immatriculation

   #@estDansParking.setter
    def setEstDansParking(self, value):
        self._estDansParking =value

    @property
    def estDansParking(self):
        return self._estDansParking == True

    #def addPlacement(self, placement):



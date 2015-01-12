from src.m.placement import Placement
class Place:
    def __init__(self):
        self._numero
        self._niveau
        self._longueur
        self._estLibre
        self.hauteur

    @property
    def numero(self):
        return self._numero
    @property
    def niveau(self):
        return self._niveau
    @property
    def longueur(self):
        return self.longueur
    @property
<<<<<<< Updated upstream
    def nbPlaceTotal(self):
        i = 0
        for t in self.l:
            i += t.nb
        return i

    @property
    def liste(self):
        return self.l




class Placement:
    def __init__(self,debut,fin):
        self.debut = debut
        self.fin = fin

=======
    def estLibre(self):
        return self.estLibre
>>>>>>> Stashed changes
    @property
    def hauteur(self):
        return self.hauteur
    @numero.setter
    def setNumero(self, value):
        self._numero = value
    @niveau.setter
    def setNiveau(self, value):
        self._numero = value
    @longueur.setter
    def setLongueur(self, value):
        self._longueur = value
    def addPlacement(self, jourDeb, moisDeb, anneeDeb, jourFin, moisFin, anneeFin):
       newplace = Placement()
       newplace.setDateDebut(jourDeb, moisDeb, anneeDeb)
       newplace.setDateFin(jourFin, moisFin, anneeFin)
       newplace.setEstEnCours(True)

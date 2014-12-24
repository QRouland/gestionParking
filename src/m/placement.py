import datetime
class Placement:

    def __init__(self):
         self._dateDebut
         self._dateFin
         self._estEnCours

    @property
    def getDateDebut(self):
        return self._dateDebut

    #@self._dateDebut.setter
    def setDateDebut(self, jour, mois, annee):
        self._dateDebut= datetime.date(jour, mois,annee)

    #@self._DateFin.setter
    def setDateFin(self, jour, mois, annee):
        self._dateFin= datetime.date(jour, mois,annee)

    #@estEnCours.setter
    def setEstEnCours(self, value):
        self._estEnCours = value

    @property
    def estEnCours(self):
        return self._estEnCours


    def partirPlace(self, value):
        self.setEstEnCours(self, False)

    @estEnCours.deleter
    def partirPlace(self):
        del self

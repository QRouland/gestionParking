import calendar

from src.m.Service import Service
from src.m.connexionBDD import connexionBDD


class Livraison(Service):
    def __init__(self, jourService, moisService, anneeService, jourDemande, moisDemande, anneeDemande, rapport,
                 categorie, idClient):
        super(Service, self).__init__(self, jourService, moisService, anneeService, jourDemande, moisDemande,
                                      anneeDemande, rapport, categorie)
        self.categorie = 3
        self.etat = 0
        # 3.Obtenir l'idVoiturier: en recherchant celui qui est disponible le jour en question
        self.idService = self.enregistrerService(self, idClient, self.categorie, self.etat)
        jour = calendar.weekday(self.dateService._day, self.dateService._month, self.dateService._year)
        connexion = connexionBDD()
        indiceVoiturier = connexion.cur.execute(
            "SELECT voiturier.idVoiturier FROM voiturier WHERE voiturier.joursDisponible = ?; ", (jour))
        idVoiturier = int(''.join(map(str, indiceVoiturier)))
        connexion.cur.execute("UPDATE service SET idVoiturier= ? WHERE idService = ?", (idVoiturier, self.idService))
        connexion.seDeconnecter()

    def effectuerLivraison(self):
        self.etat = 1
        connexion = connexionBDD()
        connexion.cur.execute("UPDATE service SET etat= 1 WHERE idService = ?", (self.idService))
        connexion.seDeconnecter()


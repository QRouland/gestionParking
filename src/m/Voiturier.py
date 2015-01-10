from src.m.connexionBDD import connexionBDD
class Voiturier:
    def __init__(self, id, nom, prenom):
        self.numero= id
        self.nom = nom
        self.prenom = prenom

    def enregistrerVoiturier(self):
        connexion = connexionBDD()
        connexion.cur =
#livraison: idClient, date, heure

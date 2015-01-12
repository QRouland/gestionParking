from src.m.connexionBDD import connexionBDD
class Abonnement:
    def __init__(self, libelle, prix, estPackGar):
        self.libelle = libelle
        self.prix = prix
        self.estPackGar = estPackGar
    def addContrat(self, contrat):
        connexion = connexionBDD()
       # indId= connexion.cur.execute("SELECT abonnement.idAbonnement FROM abonnement WHERE libelle = ? AND prix = ? AND estPackGar=?;"(self.libelle, self.prix, self.estPackGar))
       # idAbonnement = int(''.join(map(str,indId)))

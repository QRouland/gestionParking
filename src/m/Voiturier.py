import time

from src.m.connexionBDD import connexionBDD


class Voiturier:
    def __init__(self, id, nom, prenom):
        self.numero = id
        self.nom = nom
        self.prenom = prenom

    def enregistrerVoiturier(self, nom, prenom, dateEmbauche):
        connexion = connexionBDD()
        # entrée dans la base de donnée
        indiceidVoiturier = connexion.cur.execute("SELECT count(voiturier.idVoiturier) FROM voiturier;") + 1
        idVoiturier = int(''.join(map(str, indiceidVoiturier))) + 1
        connexion.cur.execute("INSERT INTO voiturier (idVoiturier,nom, prenom, dateEmbauche) VALUES (?,?,?,?);",
                              (self.idVoiturier, nom, prenom, dateEmbauche))
        connexion.seDeconnecter()

    def livrerVoiture(self):
        dateJour = time.strptime()
        connexion = connexionBDD()
        indiceLivraison = connexion.cur.execute("SELECT count(voiturier.idVoiturier) FROM voiturier;")
        idLivraison = int(''.join(map(str, indiceLivraison))) + 1
        connexion.cur.execute("INSERT INTO livraison (idLivraison,dateLivraison, idVoiturier) VALUES (?,?,?,?);",
                              (idLivraison, dateJour, self.idVoiturier))
        connexion.seDeconnecter()

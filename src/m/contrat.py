from src.m.connexionBDD import connexionBDD
class Contrat:
    def __init__(self, dateDebut, dateFin):
        self.dateDebut = dateDebut
        self.dateFin = dateFin
    def enregistrerContrat(self):

            connection = connexionBDD()
            #1.obtenir id service (fonction max de sqlite ne marche pas bien...elle ne prend en compte que le premier chiffre. Ex: max(56,9)= 9... )
            connection.cur.execute("SELECT count(service.idSercice) FROM service;")
            #entrée dans la base de donnée
            #2. obtenir l'idClient: définir une variable globale lors de l'execution du "jeu"
            #3.Obtenir l'idVoiturier: en recherchant celui qui est disponible le jour en question

            connection.cur.execute("INSERT INTO contrat (idContrat,dateDebut,dateFin, estEncours) VALUES (NULL,?,?,?);",( self.dateDebut, self.dateFin,1) )
            connection.seDeconnecter()
    def rompreContrat(self):
         connection = connexionBDD()
         connection.cur.execute("SELECT count(service.idSercice) FROM service;")
         connection.cur.execute("INSERT INTO contrat (idContrat,dateDebut,dateFin, estEncours) VALUES (NULL,?,?,?);",( self.dateDebut, self.dateFin,1) )
         connection.seDeconnecter()

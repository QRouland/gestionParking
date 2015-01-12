from src.m.connexionBDD import connexionBDD
class Contrat:
    def __init__(self, dateDebut, dateFin):
        self.dateDebut = dateDebut
        self.dateFin = dateFin
    def enregistrerContrat(self):
            connection = connexionBDD()
            connection.cur.execute("INSERT INTO contrat (idContrat,dateDebut,dateFin, estEncours) VALUES (NULL,?,?,1);",( self.dateDebut, self.dateFin,1) )
            connection.seDeconnecter()
    def rompreContrat(self, idCLient):
         connection = connexionBDD()
         indContrat  =connection.cur.execute("SELECT Contrat.idContrat FROM contrat where idClient =? AND dateDebut = ? AND dateFin=? ;"(idCLient, self.dateDebut, self.dateFin))
         idContrat= int(''.join(map(str,indContrat)))
         connection.cur.execute("Update contrat where idContrat=? set estEnCours =0;",( idContrat) )
         connection.seDeconnecter()

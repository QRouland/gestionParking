import time

import datetime
from src.m.connectionBDD import connectionBDD
class service:
    def __init__(self, jourService, moisService, anneeService, jourDemande, moisDemande, anneeDemande, rapport):
        try:
            dateService = datetime.date(anneeService, moisService,  jourService)
            self.dateService = dateService
        except:
            #Si la date n'est pas un nombre ou bien si ceux ci sont abérrents
           print ("la date de service n\'est pas correcte")
        try:
            dateDemande = datetime.date(anneeDemande, moisDemande,  jourDemande)
            self.dateDemande = dateDemande
        except:
            print  ("la date de service n\'est pas correcte")
        self.rapport = rapport
    def enregistrerService(self):
        try:
            connection = connectionBDD()
            #obtenir id service (fonction max de sqlite ne marche pas bien...elle ne prend en compte que le premier chiffre. Ex: max(56,9)= 9... )
            connection.cur.execute("SELECT count(service.idSercice) FROM service;")
            indiceidSer= connection.cur.execute("SELECT count(service.idService) FROM service;")
            idService = int(''.join(map(str,indiceidSer))) +1
            #entrée dans la base de donnée
            connection.cur.execute("INSERT INTO service (idService,dateService,dateDemande,rapport,idClient,idVoiturier,idService, idClient, idVoiturier) VALUES (?,?,?,?,?,?,?,?,?);",(idService, self.dateService, self.dateDemande, self.rapport) )
        except Exception, e:
            print str(e)
            pass






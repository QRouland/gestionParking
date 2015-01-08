import time
import calendar
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
            #1.obtenir id service (fonction max de sqlite ne marche pas bien...elle ne prend en compte que le premier chiffre. Ex: max(56,9)= 9... )
            connection.cur.execute("SELECT count(service.idSercice) FROM service;")
            #entrée dans la base de donnée
            indiceidSer= connection.cur.execute("SELECT count(service.idService) FROM service;")
            idService = int(''.join(map(str,indiceidSer))) +1
            #2. obtenir l'idClient: définir une variable globale lors de l'execution du "jeu"
            #3.Obtenir l'idVoiturier: en recherchant celui qui est disponible le jour en question
            jour= calendar.weekday(self.dateService._day, self.dateService._month, self.dateService._year)
            indiceVoiturier= connection.cur.execute("SELECT voiturier.idVoiturier FROM voiturier WHERE voiturier.joursDisponible = ?; ", (jour) )
            idVoiturier = int(''.join(map(str,indiceVoiturier )))
            connection.cur.execute("INSERT INTO service (idService,dateService,dateDemande,rapport,idClient,idVoiturier,idService, idVoiturier) VALUES (?,?,?,?,?,?,?,?,?);",(idService, self.dateService, self.dateDemande, self.rapport, idClient, idVoiturier, idService) )
            connection.seDeconnecter()
        except Exception, e:
            print str(e)
            pass






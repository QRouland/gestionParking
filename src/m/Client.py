import random
import sqlite3
import string

__author__ = 'sidya'


class Client():
    clients = []

    def __init__(self, nom, prenom, adresse, typeAbonnement):
        while True:
            id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                         range(random.randint(1, 10)))
            if Client.get(id) is None:
                break
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse
        self.clients.append(self)


    @property
    def prenom(self):
        return self.__prenom

    @property
    def nom(self):
        return self.__nom

    @property
    def id(self):
        return self.__id

    @property
    def adr(self):
        return self.__adresse

    @property
    def abonnement(self):
        return self.__typeAbonnement

    @staticmethod
    def get(id):
        for client in Client.clients:
            if client.id == id:
                return client
        return None

    @staticmethod
    def loadAll(connection):
        with connection:
            connection.row_factory = sqlite3.Row
            cur = connection.cursor()
            cur.execute("SELECT * FROM Client")
            rows = cur.fetchall()
            for row in rows:
                Client(row["num"], row["nom"], row["prenom"], row["adr"], int(row["abo"]))
        connection.close()

    @staticmethod
    def saveAll(connection):
        cur = connection.cursor()
        # reset table Client
        cur.execute("DROP TABLE IF EXISTS Client")
        cur.execute(
            """create table Client (num varchar(10) PRIMARY KEY, nom varchar(30), prenom varchar(30), adr varchar(50), abo int(1))""")
        # insert clients
        for c in Client.tous:
            cur.execute("insert into Client values (?, ?, ?, ?, ?)", (c.id, c.nom, c.prenom, c.adr, c.abonnement))
        connection.commit()
        connection.close()

    def maj(self, nom, prenom, adresse, typeAbonnement):
        self.__nom = nom
        self.__prenom = prenom
        self.__typeAbonnement = typeAbonnement
        self.__adresse = adresse

    def __str__(self):
        return "( " + self.__id + ", " + self.__nom + ", " + self.__prenom + ", " + self.__adresse + ", " + str(
            self.__typeAbonnement) + " )"




"""
    Module de gestion de la base de Donnée Sqlite
"""
from shutil import copyfile
import sqlite3

## Classe de connexion a la bd
class connexionBDD:
    __chemin = "src/m/BDDprojetPython.sq3"
    __sql = "src/m/table.sql"

    ## Construeur de la connexion. Initialise la bd en cas d'inexistance
    def __init__(self):
        try:
            with open(self.__chemin):
                pass
        except IOError:
            self.__conn = sqlite3.connect(connexionBDD.__chemin)
            self.__conn.row_factory = sqlite3.Row
            self.__cur = self.__conn.cursor()
            self.initialisationBDD()
        self.__conn = sqlite3.connect(connexionBDD.__chemin)
        self.__conn.row_factory = sqlite3.Row
        self.__cur = self.__conn.cursor()

    ## Execute une requete avec des param
    # @param req la requete a execute
    # @param param un tuple contenant les donnees a inserer dans la requete
    def execute(self, req, param=()):
        try:
            r = self.__cur.execute(req, param)
            self.__conn.commit()
        except Exception as e:
            print (e)
            r = None
        return r

    ## Id genere par la derniere requete
    # @return Id genere par la derniere requete
    def lastId(self):
        return self.__cur.lastrowid

    ## Deconnexion de la BD
    def seDeconnecter(self):
        self.__cur.close()
        self.__conn.close()

    ## Initialise la BD
    def initialisationBDD(self):
        with open(self.__sql) as f:
            sql = f.read()
            self.__conn.executescript(sql)
            self.__conn.commit()
    ## Creer une copie de la bd
    # @param path le chemin du fichier de sauvegarde de la bd
    @staticmethod
    def sauver(path):
        copyfile(connexionBDD.chemin, path)

    ## Charge une copie de la bd
    # @param path le chemin du fichier a charger pour la bd
    @staticmethod
    def charger(path):
        copyfile(path, connexionBDD.chemin)

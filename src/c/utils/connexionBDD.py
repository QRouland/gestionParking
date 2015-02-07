from shutil import copyfile
import sqlite3


class connexionBDD:
    __chemin = "m/BDDprojetPython.sq3"
    __sql = "m/table.sql"

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


    def execute(self, req, param=()):
        r = None
        # try:
        r = self.__cur.execute(req, param)
        self.__conn.commit()
        """except Exception as e:
            print (e)"""
        return r

    def lastId(self):
        return self.__cur.lastrowid

    def seDeconnecter(self):
        self.__cur.close()
        self.__conn.close()

    def initialisationBDD(self):
        with open(self.__sql) as f:
            sql = f.read()
            self.__conn.executescript(sql)
            self.__conn.commit()

    @staticmethod
    def sauver(path):
        copyfile(connexionBDD.chemin, path)

    @staticmethod
    def charger(path):
        copyfile(path, connexionBDD.chemin)

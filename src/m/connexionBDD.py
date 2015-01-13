__author__ = 'sidya'

import sqlite3

class connexionBDD:
    def __init__(self):
        self.__chemin = "m/BDDprojetPython.sq3"
        self.__conn = sqlite3.connect(self.__chemin)
        self.__conn.row_factory = sqlite3.Row
        self.__cur = self.__conn.cursor()

    def execute(self, req, param = ()):
        r = None
        #try:
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
        with open("m/table.sql") as f:
            sql  = f.read()
            self.__conn.executescript(sql)
            self.__conn.commit()

import sqlite3
class connexionBDD:
    def __init__(self):
        self.chemin = "BDDprojetPython.sq3"
        self.conn =sqlite3.connect(self.chemin)
        self.cur =self.conn.cursor()
    def seDeconnecter(self):
       self.cur.close()
       self.conn.close()
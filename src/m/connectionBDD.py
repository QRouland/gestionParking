import sqlite3
class connectionBDD:
    def __init__(self):
        self.chemin = "/Users/nadiel/SQLite/BDDprojetPython.sq3"
        self.conn =sqlite3.connect(self.chemin)
        self.cur =self.conn.cursor()
    def seDeconnecter(self):
       self.cur.close()
       self.conn.close()
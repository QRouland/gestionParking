__author__ = 'sidya'

class connexionBDD :
    def __init__(self):
        try:
            self.__conn = sqlite3.connect("BD.sql3")
            self.__cur = self.__conn.cursor()
        except Exception as e :
            pass # later

    def seDeconnecter(self):
        self.__cur.close()
        self.__conn.close()

    def execute(self, req):
        try:
            r = self.__cur.execute(req)
            self.__conn.commit()
        except Exception as e :
            pass # later
        return r


    def lastId(self):
        return self.__cur.lastrowid
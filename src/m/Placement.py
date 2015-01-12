import datetime
import random
import string

__author__ = 'sidya'

class Placement:
    placements = []
    def __init__(self,voiture, place):
        """
        Creer un placement
        :param voiture: Voiture
        :param place: Place
        :return:
        """
        while True :
            id =''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(1,10)))
            if Placement.get(id) is None:
                break
        self.__id = id
        self.__voiture = voiture
        self.__place = place
        self.__debut = datetime.datetime
        self.__fin = None
        place.prendre()
        self.placements.append(self)

    def end(self):
        self.__fin = datetime.datetime
        self.__place.liberer()

    @property
    def id(self):
        return self.__id

    @staticmethod
    def get(id):
        """
        Recupere le Placement d'id id
        :param id: str
        :return: Placement or None
        """
        for p in Placement.placements:
            if p.__id == id:
                return p
        return None

    @property
    def estEnCours(self):
        return datetime.datetime < self.__fin

__author__ = 'sidya'


class Place:
    """
    Representation d'une place
    """

    def __init__(self, numero, niveau, longueur, hauteur):
        """
        Creer une place.
        Les dimensions doivent etre données en cm (longueur, hauteur)
        :param numero: int
        :param niveau: int
        :param longueur: int
        :param hauteur: int
        :return:
        """
        self.__numero = numero
        self.__niveau = niveau
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__estLibre = True
        self.__estSuperAbo = False
        self.__Placement = None

    @property
    def estLibre(self):
        return self.__estLibre

    @property
    def estReserver(self):
        return self.__estSuperAbo

    def dimValide(self, h, l):
        """
        Retourn si un element de hauteur (cm) h et de longueur(cm) l passe dans la place
        :param h: int
        :param l: int
        :return: bool
        """
        return h < self.__hauteur and l < self.__longueur

    def superAbo(self):
        """
        Renvoit si la place est une place superAbo
        :return: bool
        """
        if (self.__estSuperAbo == True):
            raise Exception("Place déjà reservé")
        self.__estSuperAbo = True


    def prendre(self):
        """
        Rend la place indisponible
        :param Placement:
        :return:
        """
        if (self.__estLibre == False):
            raise Exception("Place déjà prise")
        self.__estLibre = False

    def liberer(self):
        """
        Libere une place non dispo
        :return:
        """
        if (self.__estLibre == True):
            raise Exception("Impossible de liberer une place vide")
        self.__estLibre = True









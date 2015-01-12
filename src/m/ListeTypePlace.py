__author__ = 'sidya'

class ListeTypePlace:
    """
        Classe qui permet de définir une liste de type de place par niveau pour la création d'un parking
    """

    def __init__(self):
        self.l = []

    def add(self, h, l, nb):
        self.l.append(TypePlace(h, l, nb))

    @property
    def nbPlaceTotal(self):
        i = 0
        for t in self.l:
            i += t.nb
        return i

    @property
    def liste(self):
        return self.l

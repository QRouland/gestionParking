from src.m.Voiture import Voiture

__author__ = 'sidya'

from nose.tools import assert_equal



class TestVoiture :
    def TestVoiture(self):
        v = Voiture(None,None,120,100,"IMMA")
        assert_equal(v.longueur, 120, "Ne retourne pas la longueur attendue")
        assert_equal(v.hauteur, 100, "Ne retourne pas la hateur attendue")
        assert_equal(v.immatriculation, "IMMA", "Ne retourne pas l'immatriculation attendue")
        id = v.id

        #Recuperer une Voiture Non existant
        try:
            t = Voiture("aaaa")
            assert_equal(True, False, "Un id invalide pour une voiture doit lever une exection")
        except IndexError :
            pass

        #Recuperer un Voiture existant
        try:
            t = Voiture(id)
        except IndexError :
            assert_equal(True, False, "Un id valide pour une voiture ne doit pas lever une exection")
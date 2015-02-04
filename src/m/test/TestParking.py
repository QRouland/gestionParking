__author__ = 'sidya'

from nose.tools import assert_equal

from src.m.Parking import Parking, TypePlace, Place

class TestParking :
    def TestParking(self):
        p = Parking(None,"test",[TypePlace(None,220,200,4,2.5,1),TypePlace(None,200,130,5,2.5,1)])
        id = p.id
        assert_equal(p.nbPlacesLibresParking, 9, "Nombre de place libre non valide")
        assert_equal(p.nbPlaces, 9, "Nombre de place  non valide")
        assert_equal(p.nbSuperAbo, 0, "Nombre de place super abo")

    def TestRecherchePlace(self):
        pass

class TestPlace :
    def TestPlace(self):
        t1 =TypePlace(None,220,200,4,2.5,1)
        parking = Parking(None,"test",[t1])

        p = Place(None,parking,t1,2,1)

    def TestPrendreLiberer(self):
        t1 = TypePlace(None,220,200,4,2.5,1)
        parking = Parking(None,"test",[t1])

        p = Place(None,parking,t1,2,1)

        assert_equal(p.estlibre, True, "La place devrait etre libre")

        p.prendre()
        assert_equal(p.estlibre, False, "La place ne devrait ne pas etre libre")

        try:
            p.prendre()
            assert_equal(True, False, "Une place prise ne peut pas a nouveau prise")
        except Exception :
            pass

        p.liberer()
        assert_equal(p.estlibre, True, "La place devrait etre libre")

        try:
            p.liberer()
            assert_equal(True, False, "Une place libre ne peut pas a nouveau liberée")
        except Exception :
            pass


class TestTypePlace :
    def TestTypePlace(self):
        #Creation
        t = TypePlace(None,220,200,4,2.5,1)
        assert_equal(t.longueur, 220, "Valeur non attendue pour la longueur")
        assert_equal(t.hauteur, 200,"Valeur non attendue pour la hauteur")
        assert_equal(t.nombre,4,"Valeur non attendue pour le nombre de place")
        assert_equal(t.prix, 2.5,"Valeur non attendue pour le prix")
        assert_equal(t.niveau, 1, "Valeur non attendue pour le niveau")
        id = t.id

        #Recuperer un TypePlace Non existant
        try:
            t = TypePlace("aaaa")
            assert_equal(True, False, "Un id invalide pour une type de place doit lever une exection")
        except IndexError :
            pass

        #Recuperer un TypePlace existant
        try:
            t = TypePlace(id)
        except IndexError :
            assert_equal(True, False, "Un id valide pour une type de place ne doit pas lever une exection")
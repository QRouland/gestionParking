"""
    Test Module m/Service
"""
import datetime
from nose.tools import assert_equal,assert_not_equal
from src.m.Abonnement import Client, TypeAbonnement
from src.m.Parking import Placement, Place, Parking, TypePlace
from src.m.Service import Service, TypeService
from src.m.Voiture import Voiture

## Test des Service
class TestService:
    ## Test instanciation
    def TestService(self):
        v = Voiture(None, None, 120, 100, "IMMA")
        t  = TypePlace(None, 220, 200, 4, 2.5, 1)
        place = Place(None,Parking(None, "test", [t]),t,2)
        placemnent = Placement(None,v,place)
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        s = Service(None, c, placemnent, TypeService.ENTRETIEN)
        assert_equal(s.estRealise, False)
        assert_equal(s.typeService, TypeService.ENTRETIEN)
        assert_equal(s.placement,placemnent)

    def TestModifService(self):
        v = Voiture(None, None, 120, 100, "IMMA")
        t  = TypePlace(None, 220, 200, 4, 2.5, 1)
        place = Place(None,Parking(None, "test", [t]),t,2)
        placemnent = Placement(None,v,place)
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        s = Service(None, c, placemnent, TypeService.LIVRAISON, datetime.time(),"Miraol")

        time = datetime.time()
        s.maj(time,"autre")
        assert_equal(s.lieu,"autre")
        assert_equal(s.dateService,time)

    def TestDoService(self):
        v = Voiture(None, None, 120, 100, "IMMA")
        t  = TypePlace(None, 220, 200, 4, 2.5, 1)
        place = Place(None,Parking(None, "test", [t]),t,2)
        placemnent = Placement(None,v,place)
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        s = Service(None, c, placemnent, TypeService.LIVRAISON, datetime.time(),"Miraol")
        assert_equal(s.estRealise, False)
        s.doService()
        assert_equal(s.estRealise, True)



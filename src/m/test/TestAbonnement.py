"""
    Test Module Abonnement
"""


from src.m.Abonnement import Client, TypeAbonnement
from nose.tools import assert_equal,assert_not_equal

## Test Client
class TestClient:
    ## Test Instenciations
    def TestClient(self):
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        id = c.id
        assert_equal(c.nom,"Jean")
        assert_equal(c.prenom,"Paul")
        assert_equal(c.cb,"1225233")
        assert_equal(c.abonnement,TypeAbonnement.ABONNE)

        c = Client(id)
        assert_equal(c.nom,"Jean")
        assert_equal(c.prenom,"Paul")
        assert_equal(c.cb,"1225233")
        assert_equal(c.abonnement,TypeAbonnement.ABONNE)

    ## Test mise a jour Client
    def TestMaj(self):
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        c.maj("lulu","ez","45646",TypeAbonnement.SUPER_ABONNE)
        assert_equal(c.nom,"lulu")
        assert_equal(c.prenom,"ez")
        assert_equal(c.cb,"45646")
        assert_equal(c.abonnement,TypeAbonnement.SUPER_ABONNE)

    ## Test desabonnement
    def TestDesabo(self):
        c = Client(None,"Jean","Paul","1225233",TypeAbonnement.ABONNE)
        c.desabo()
        try :
            Client(c.id)
            assert_equal(False,True)
        except IndexError :
            pass
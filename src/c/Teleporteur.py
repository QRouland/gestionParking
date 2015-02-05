from src.m.Parking import Placement

__author__ = 'sidya'


class Teleporteur:
    @staticmethod
    def teleporterVoiture(voiture, place):
        p = Placement(None, voiture, place)
        place.prendre()
        return p

    @staticmethod
    def teleporterVoitureSuperAbonne(voiture, parking):
        place = parking.addPlaceSuperAbo(parking)
        p = Placement(None, voiture, place)
        return p

    @staticmethod
    def teleporterVersSortie(placement):
        placement.end()

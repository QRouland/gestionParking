from src.m.Parking import Placement

__author__ = 'sidya'


class Teleporteur:
    @staticmethod
    def teleporterVoiture(voiture, place):
        p = Placement(None,voiture, place)
        place.prendre()
        return p.id

    @staticmethod
    def teleporterVoitureSuperAbonne(voiture, parking):
        place = parking.addPlaceSuperAbo()
        p = Placement(None, voiture, place)
        return p.id

    @staticmethod
    def teleporterVersSortie(placement):
        placement.end()

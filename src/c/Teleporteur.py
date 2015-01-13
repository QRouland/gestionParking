from src.m.Parking import Placement

__author__ = 'sidya'


class Teleporteur:
    @staticmethod
    def teleporterVoiture(voiture, place):
        p = Placement(None,voiture, place,None,None)
        return p.id

    @staticmethod
    def teleporterVoitureSuperAbonne(voiture):
        pass

    @staticmethod
    def teleporterVersSortie(placement):
        placement.end()
from src.m.Placement import Placement

__author__ = 'sidya'


class Teleporteur:
    @classmethod
    def teleporterVoiture(self, voiture, place):
        p = Placement(voiture, place)
        return p.id

    @classmethod
    def teleporterVoitureSuperAbonne(self, voiture):
        pass

    @classmethod
    def teleporterVersSortie(self, placement):
        placement.end()
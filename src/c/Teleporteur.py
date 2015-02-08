"""
    Gestion de teleportation de voiture
"""
from src.m.Parking import Placement


## Gestion de teleportation de Voiture
class Teleporteur:
    ## Teleportation d'une voiture standars
    # @param voiture Voiture a garer
    # @param place Place ou garer la voiture
    # @return Placement creer
    @staticmethod
    def teleporterVoiture(voiture, place):
        p = Placement(None, voiture, place)
        place.prendre()
        return p
    ## Teleportation d'une voiture d'un superAbo
    # @param voiture Voiture a garer
    # @param parking Parking ou garer la voiture
    # @return Placement creer
    @staticmethod
    def teleporterVoitureSuperAbonne(voiture, parking):
        place = parking.addPlaceSuperAbo(parking)
        p = Placement(None, voiture, place)
        return p
    ## Teleportation de la voiture vers la sortie
    # @param placement Placement de lavoiture que l'on veut sortir
    @staticmethod
    def teleporterVersSortie(placement):
        placement.end()

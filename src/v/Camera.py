"""
    Module de simaultaion d'une camera
"""

import random
import string
from src.m.Voiture import Voiture

## Une Camera
class Camera:
    ## Retourne une voiture genere aleatoirement de longueur entre 150 et 300 cm et de hauteur entre 100 et 200 cm
    @staticmethod
    def donnerVoiture():
        v = Voiture(None, None, random.randint(150, 300), random.randint(100, 200), ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
            range(random.randint(5, 10))))
        return v

import random
import string

from src.m.Voiture import Voiture


__author__ = 'sidya'


class Camera:
    @classmethod
    def donnerVoiture(self):
        v = Voiture(random.randint(150, 300), random.randint(100, 200), ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
            range(random.randint(1, 10))),False)
        return v

import random
import string
from src.m.Voiture import Voiture

class Camera:
    @staticmethod
    def donnerVoiture():
        v = Voiture(None, None, random.randint(150, 300), random.randint(100, 200), ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
            range(random.randint(5, 10))))
        return v

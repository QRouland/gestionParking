from src.m.camera import Camera

__author__ = 'sidya'

import nose
class testCamera :
    def run(self):
        pass

    def testTailleMax(self):
        c = Camera()
        assert (c.capturerHauteur()>1.5)

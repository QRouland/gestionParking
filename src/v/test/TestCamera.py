from src.m.camera import Camera

__author__ = 'sidya'

from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class testCamera:
    def test_TailleMax(self):
        c = Camera()
        assert_equal(c.capturerHauteur()<2.5)

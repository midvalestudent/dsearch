''' Test something
'''
from unittest import TestCase

from .context import example


class TestExample(TestCase):
    def test_init(self):
        self.assertTrue(True)

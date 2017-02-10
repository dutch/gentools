from unittest import TestCase
from gentools.command_line import genconf


class TestGenconf(TestCase):
    def test_basic(self):
        genconf()

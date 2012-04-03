import unittest

from ano_bissexto import eh_bissexto

class AnoBissextoTestCase(unittest.TestCase):
    def test_1900_nao_eh_bissexto(self):
        self.assertFalse(eh_bissexto(1900))

    def test_2000_eh_bissexto(self):
        self.assertTrue(eh_bissexto(2000))

    def test_2012_eh_bissexto(self):
        self.assertTrue(eh_bissexto(2012))

    def test_1600_eh_bissexto(self):
        self.assertTrue(eh_bissexto(1600))

    def test_1955_nao_eh_bissexto(self):
        self.assertFalse(eh_bissexto(1955))

unittest.main()

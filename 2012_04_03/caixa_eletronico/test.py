import unittest
from caixa_eletronico import sacar_dinheiro


class CaixaEletronicoTestCase(unittest.TestCase):

    def test_10_reais_deve_retornar_uma_nota_de_10(self):
        self.assertEqual({10:1}, sacar_dinheiro(10))

    def test_20_reais_deve_retornar_uma_nota_de_20(self):
        self.assertEqual({20:1}, sacar_dinheiro(20))

    def test_50_reais_deve_retornar_uma_nota_de_50(self):
        self.assertEqual({50:1}, sacar_dinheiro(50))

    def test_60_reais_deve_retornar_uma_nota_de_50_e_1_de_10(self):
        self.assertEqual({50:1, 10:1}, sacar_dinheiro(60))

    def test_70_reais_deve_retornar_uma_nota_de_50_e_outra_de_20(self):
        self.assertEqual({50:1, 20:1}, sacar_dinheiro(70))

    def test_90_reais_deve_retornar_uma_nota_de_50_e_duas_de_20(self):
        self.assertEqual({50:1, 20:2}, sacar_dinheiro(90))

    def test_100_reais_deve_retornar_uma_de_100(self):
        self.assertEqual({100:1}, sacar_dinheiro(100))

    def test_370_reais_deve_retornar_3_de_100_e_1_de_50_e_1_de_20(self):
        self.assertEqual({100:3, 50:1, 20:1}, sacar_dinheiro(370))


unittest.main()

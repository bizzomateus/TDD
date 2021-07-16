from unittest import TestCase
from src.leilao.dominio import Avaliador, Usuario, Lance, Leilao

class TestAvaliador(TestCase):

    def test_avalia(self):
        mat = Usuario('Mateus')
        re = Usuario('Regina')

        lance_mat = Lance(mat, 100.00)
        lance_re = Lance(re, 150.00)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_mat)
        leilao.lances.append(lance_re)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        min_esperado = 100.00
        max_esperado = 150.00

        self.assertEqual(max_esperado, avaliador.maior_lance)
        self.assertEqual(min_esperado, avaliador.menor_lance)

        
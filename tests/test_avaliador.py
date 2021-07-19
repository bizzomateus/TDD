from unittest import TestCase
from src.leilao.dominio import Avaliador, Usuario, Lance, Leilao

class TestAvaliador(TestCase):

    def test_avalia_crescente(self):
        '''
            deve avaliar lances adicionados em ordem crescente
        '''
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

    def test_avalia_decrescente(self):
        '''
            deve avaliar lances adicionados em ordem decrescente
        '''
        mat = Usuario('Mateus')
        re = Usuario('Regina')

        lance_mat = Lance(mat, 100.00)
        lance_re = Lance(re, 150.00)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_re)
        leilao.lances.append(lance_mat)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        min_esperado = 100.00
        max_esperado = 150.00

        self.assertEqual(max_esperado, avaliador.maior_lance)
        self.assertEqual(min_esperado, avaliador.menor_lance)

    def test_avalia_mesmo_valor(self):
        '''
            deve retornar mesmo valor para maior e menor lance
            quando só ouver um único lance
        '''
        valor_esperado = 1000.0

        user = Usuario('Mat')
        lance = Lance(user, valor_esperado)

        leilao = Leilao('Carro')
        leilao.lances.append(lance)

        
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(valor_esperado, avaliador.menor_lance)
        self.assertEqual(valor_esperado, avaliador.maior_lance)

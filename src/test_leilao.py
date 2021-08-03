from unittest import TestCase
from leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.mat = Usuario('Mateus')
        self.lance_mat = Lance(self.mat, 100.00)
        self.leilao = Leilao('Celular')

    def test_avalia_crescente(self):
        '''
            deve avaliar lances adicionados em ordem crescente
        '''
        re = Usuario('Regina')
        lance_re = Lance(re, 150.00)

        self.leilao.propoe(self.lance_mat)
        self.leilao.propoe(lance_re)

        min_esperado = 100.00
        max_esperado = 150.00

        self.assertEqual(max_esperado, self.leilao.maior_lance)
        self.assertEqual(min_esperado, self.leilao.menor_lance)

    def test_avalia_decrescente(self):
        '''
            deve avaliar lances adicionados em ordem decrescente
        '''
        re = Usuario('Regina')
        lance_re = Lance(re, 150.00)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_re)
            self.leilao.propoe(self.lance_mat)


    def test_avalia_mesmo_valor(self):
        '''
            deve retornar mesmo valor para maior e menor lance
            quando só ouver um único lance
        '''
        valor_esperado = 100.00
        self.leilao.propoe(self.lance_mat)

        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)

    def test_avalia_tres_lances(self):
        '''
            deve avaliar tres lances adicionados intercalados
        '''
        futuro = Usuario('Futuro')
        re = Usuario('Regina')

        lance_futuro = Lance(futuro, 200.00)
        lance_re = Lance(re, 150.00)

        self.leilao.propoe(lance_futuro)
        self.leilao.propoe(lance_re)
        self.leilao.propoe(self.lance_mat)

        min_esperado = 100.00
        max_esperado = 200.00

        self.assertEqual(max_esperado, self.leilao.maior_lance)
        self.assertEqual(min_esperado, self.leilao.menor_lance)


    def test_permite_se_nao_tem_lance_anterior(self):
        self.leilao.propoe(self.lance_mat)

        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances)


    def test_permite_caso_ultimo_usuario_seja_diferente(self):
        regina = Usuario('Regina')
        lance_regina = Lance(regina, 200.00)

        self.leilao.propoe(self.lance_mat)
        self.leilao.propoe(lance_regina)

        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances)


    def test_nao_permite_lance_quando_mesmo_usuario(self):
        lance_mat_300 = Lance(self.mat,300.00)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_mat)
            self.leilao.propoe(lance_mat_300)

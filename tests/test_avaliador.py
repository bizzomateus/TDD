from unittest import TestCase

class TestAvaliador(TestCase):

    def test_avalia(self):
        # valor esperado/valor_informado
        valor_esperado = 1
        valor_informado = 1
        self.assertEqual(valor_esperado,valor_informado)

        
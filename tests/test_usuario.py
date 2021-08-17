from src.leilao.excecoes import LanceInvalido
from src.leilao.dominio import Leilao, Usuario

import pytest

@pytest.fixture
def mateus():
    return Usuario('Mateus', 200)


@pytest.fixture
def leilao():
    return Leilao('Brinquedos')

def test_subtrai_valor_da_carteira_quando_propoe_lance(mateus, leilao):
    mateus.propoe_lance(leilao, 100)

    assert mateus.carteira == 100


def test_permite_lance_quando_valor_igual_a_carteira(mateus, leilao):
    mateus.propoe_lance(leilao, 200)

    assert mateus.carteira == 0


def test_nao_permite_lances_com_valor_maior_que_carteira(mateus, leilao):
    with pytest.raises(LanceInvalido):
        mateus.propoe_lance(leilao, 300)

        assert mateus.carteira == 200

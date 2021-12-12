from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido
import pytest


@pytest.fixture  # Serve pra declarar que é uma fixture, sendo passado como argumento nas funções de testes
def vini():
    return Usuario('Vini', 100.0)


@pytest.fixture  # Serve pra declarar que é uma fixture, sendo passado como argumento nas funções de testes
def leilao():
    return Leilao('Celular')


def test_Quando_OUsuarioProporUmLance_Deve_SubtrairOValorDeSuaCarteira(vini, leilao):  # Fixtures como argumentos
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_Quando_OValorEhMenorQueODaCarteira_Deve_PermitirProporOLance(vini, leilao):  # Fixtures como argumentos
    vini.propoe_lance(leilao, 1)

    assert vini.carteira == 99.0


def test_Quando_OValorEhIgualAoDaCarteira_Deve_PermitirProporOLance(vini, leilao):  # Fixtures como argumentos
    vini.propoe_lance(leilao, 100)

    assert not vini.carteira


def test_Quando_OValorEhMaiorQueODaCarteira_Deve_ImpedirDeProporOLance(vini, leilao):  # Fixtures como argumentos
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200)

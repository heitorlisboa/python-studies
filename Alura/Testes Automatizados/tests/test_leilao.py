from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido
from unittest import TestCase


class TestLeilao(TestCase):

    def setUp(self):  # Sempre executado ANTES de uma função de testes.
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def tearDown(self):  # Sempre executado APÓS uma função de testes.
        pass

    @classmethod
    def setUpClass(cls):  # Executado na CRIAÇÃO DA CLASSE, sendo executado uma única vez.
        pass

    @classmethod
    def tearDownClass(cls):  # Executado após a ÚLTIMA FUNÇÃO de testes ser executada.
        pass

    def test_Quando_AdicionadosEmOrdemCrescente_Deve_RetornarOMaiorEOMenorLances(self):
        yuri = Usuario('Yuri', 500.0)

        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_Quando_AdicionadosEmOrdemDecrescente_Deve_RetornarLanceInvalido(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_Quando_OLeilaoTiverUmLance_Deve_RetornarOMesmoValorParaMenorEMaiorLances(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_Quando_OLeilaoTiverTresLances_Deve_RetornarOMenorEOMaiorLances(self):
        yuri = Usuario('Yuri', 500.0)
        vini = Usuario('Vini', 500.0)

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_Quando_UmMesmoUsuarioProporDuasVezesSeguidas_Deve_RetornarLanceInvalido(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)


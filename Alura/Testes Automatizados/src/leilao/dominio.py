from src.leilao.excecoes import LanceInvalido


class Usuario:
    def __init__(self, nome: str, carteira: float or int = 0):
        self._nome = nome
        self._carteira = carteira

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def carteira(self) -> float or int:
        return self._carteira

    def _valida(self, valor):
        if valor <= self._carteira:
            return True

        raise LanceInvalido('Não é possível propor um valor maior que o disponível na carteira!')

    def propoe_lance(self, leilao, valor: float or int):
        if self._valida(valor):
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self._carteira -= valor


class Lance:
    def __init__(self, usuario: Usuario, valor: float or int):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao: str):
        self.descricao = descricao
        self._lances = []
        self._maior_lance = 0.0
        self._menor_lance = 0.0

    @property
    def lances(self) -> list:
        return self._lances.copy()

    @property
    def maior_lance(self):
        return self._maior_lance

    @property
    def menor_lance(self):
        return self._menor_lance

    def _valida(self, lance):
        if self._nao_tem_lances():
            self._menor_lance = lance.valor
            self._maior_lance = lance.valor
            return True

        if self._lance_eh_maior_que_o_anterior(lance) and self._usuario_diferente(lance):
            self._maior_lance = lance.valor
            return True

    def _nao_tem_lances(self):
        return not self._lances  # Como uma lista vazia retorna False, pode-se fazer dessa maneira.

    def _lance_eh_maior_que_o_anterior(self, lance):
        if lance.valor > self._maior_lance:
            return True

        raise LanceInvalido('O lance deve ser maior que o do último usuário!')

    def _usuario_diferente(self, lance):
        ultimo_lance: Lance = self._lances[-1]
        if lance.usuario != ultimo_lance.usuario:
            return True

        raise LanceInvalido('Um mesmo usuário não pode propor dois lances seguidos!')

    def propoe(self, lance_atual: Lance):
        if self._valida(lance_atual):
            self._lances.append(lance_atual)

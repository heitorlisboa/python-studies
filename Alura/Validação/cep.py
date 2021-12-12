import requests
import re


class CEP:
    def __init__(self, cep: str or int) -> None:
        cep = str(cep)

        if self._valida(cep):
            self.cep = self._somente_digitos(cep)
        else:
            raise ValueError('CEP inválido!')

    def __str__(self) -> str:
        cep_formatado = f'{self.cep[:5]}-{self.cep[5:]}'

        return cep_formatado

    def _valida(self, cep):
        padrao_cep = re.compile('[0-9]{5}[-]?[0-9]{3}')
        match = padrao_cep.match(cep)
        match = match.group() == cep
        dados = self._acessa_via_cep(cep)

        if match and not 'erro' in dados:
            self.dados_cep = dados
            return True

        return False

    def _acessa_via_cep(self, cep):
        cep = self._somente_digitos(cep)
        url = f'https://viacep.com.br/ws/{cep}/json'
        r = requests.get(url)
        dados = r.json()

        return dados

    @staticmethod
    def _somente_digitos(num: str) -> str:
        num = ''.join([x for x in num if x.isdigit()])

        return num


if __name__ == '__main__':
    cep = '24900-185'
    objeto = CEP(cep)
    print(objeto.dados_cep)

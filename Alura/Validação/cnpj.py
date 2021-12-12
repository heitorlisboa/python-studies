import re
from basedoc import BaseDoc

class CNPJ(BaseDoc):
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self._valida(cnpj):
            cnpj = self._somente_digitos(cnpj)
            self._cnpj = self._formata(cnpj)
        else:
            raise ValueError('CNPJ invalido!')

    def __str__(self) -> str:
        return self._cnpj
    
    @staticmethod
    def _valida_entrada(doc: str) -> bool:
        # 99.999.999/9999-99
        padrao_cnpj = re.compile('[0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2}')
        match = padrao_cnpj.match(doc)

        return match

    @staticmethod
    def _gera_primeiro_digito(doc: str) -> str:
        # multiplicadores = [x for x in range(5, 1, -1)] + [x for x in range(9, 1, -1)]
        multiplicadores = list(range(5, 1, -1)) + list(range(9, 1, -1))
        soma = 0

        for i in range(0, 12):
            soma += int(doc[i]) * multiplicadores[i]
        
        resto = soma % 11

        if resto < 2:
            resto = 0
        else:
            resto = 11 - resto
        
        return str(resto)

    @staticmethod
    def _gera_segundo_digito(doc: str) -> str:
        # multiplicadores = [x for x in range(6, 1, -1)] + [x for x in range(9, 1, -1)]
        multiplicadores = list(range(6, 1, -1)) + list(range(9, 1, -1))
        soma = 0

        for i in range(0, 13):
            soma += int(doc[i]) * multiplicadores[i]
        
        resto = soma % 11

        if resto < 2:
            resto = 0
        else:
            resto = 11 - resto
        
        return str(resto)

    @staticmethod
    def _formata(doc: str) -> str:
        # 99.999.999/9999-99
        cnpj_formatado = '{}.{}.{}/{}-{}'.format(
            doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[12:]
        )

        return cnpj_formatado
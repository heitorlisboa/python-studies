import re
from basedoc import BaseDoc

class CPF(BaseDoc):
    def __init__(self, cpf):
        cpf = str(cpf)
        if self._valida(cpf):
            cpf = self._somente_digitos(cpf)
            self._cpf = self._formata(cpf)
        else:
            raise ValueError('CPF inválido!')
    
    def __str__(self) -> str:
        return self._cpf
        
    @staticmethod
    def _valida_entrada(doc: str) -> bool:
        # 999.999.999-99
        padrao_cpf = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')
        match = padrao_cpf.match(doc)

        return match
    
    @staticmethod
    def _gera_primeiro_digito(doc: str) -> str:
        soma = 0

        for i in range(10, 1, -1):
            soma += int(doc[10 - i]) * i
        
        resto = (soma * 10) % 11

        if resto == 10:
            resto = 0

        return str(resto)

    @staticmethod
    def _gera_segundo_digito(doc: str) -> str:
        soma = 0

        for i in range(11, 1, -1):
            soma += int(doc[11 - i]) * i
        
        resto = (soma * 10) % 11

        if resto == 10:
            resto = 0

        return str(resto)

    @staticmethod
    def _formata(doc: str) -> str:
        # 999.999.999-99
        cpf_formatado = '{}.{}.{}-{}'.format(
            doc[:3], doc[3:6], doc[6:9], doc[9:]
        )

        return cpf_formatado

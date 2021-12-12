from abc import ABCMeta, abstractmethod

class BaseDoc(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def _valida(self, doc: str='') -> bool:
        if not self._valida_entrada(doc):
            return False
        
        doc = self._somente_digitos(doc)
        
        if self._checa_digitos_repetidos(doc):
            return False

        return self._gera_primeiro_digito(doc) == doc[-2] \
            and self._gera_segundo_digito(doc) == doc[-1]
    
    @abstractmethod  # @staticmethod
    def _valida_entrada(doc: str) -> bool:
        pass

    @abstractmethod  # @staticmethod
    def _gera_primeiro_digito(doc: str) -> str:
        pass

    @abstractmethod  # @staticmethod
    def _gera_segundo_digito(doc: str) -> str:
        pass

    @staticmethod
    def _checa_digitos_repetidos(doc: str) -> bool:
        # Transforma em lista
        doc = [digito for digito in doc]
        
        # Se a o set dessa lista só tiver um dígito, significa que a lista é composta
        # pela repetição de um único dígito. Assim o set terá tamanho = 1, retornando True.
        return len(set(doc)) == 1

    @abstractmethod  # @staticmethod
    def _formata(doc: str) -> str:
        pass

    @staticmethod
    def _somente_digitos(doc: str) -> str:
        doc = ''.join([x for x in doc if x.isdigit()])

        return doc

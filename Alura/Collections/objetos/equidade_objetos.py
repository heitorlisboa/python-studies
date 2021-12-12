from abc import ABCMeta, abstractmethod


# >>> IMPORTANTE <<<
# NÃO SE DEVE UTILIZAR VARIOS '__eq__' DIFERENTES COMO FIZ NESSE CÓDIGO,
# SOMENTE COLOQUEI DIFERENTES PARA EXEMPLIFICAR DIFERENTES MANEIRAS,
# MANTENHA UM MESMO PADRÃO NOS '__eq__'!!!
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __str__(self):
        return f'>>Codigo {self._codigo} Saldo {self._saldo}<<'

    def __eq__(self, other):
        return isinstance(other, Conta)
        # Isso significa que retorna 'True' caso o 'other' (objeto com qual irá se comparar)
        # é da classe 'Conta' ou de qualquer uma de suas classes filhas.

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def passar_o_mes(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)

    def __eq__(self, other):  # Nesse caso, o '__eq__' sobrepõe o da classe 'Conta'.
        return type(other) == ContaCorrente
        # Isso significa que retorna 'True' somente se for exatamente a mesma classe.

    def passar_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)

    def __eq__(self, other):
        if not isinstance(other, Conta):
            return False
        
        # Neste 'return' a seguir, eu estava tendo problemas pois com o uso de dois underlines,
        # não conseguia acessar os atributos da classe mãe, então seria necessário redeclará-los.
        # Para contornar o problema, coloquei apenas um underline, para manter indicando que o
        # atributo é privado, mas não ser "impedido" de alcançá-lo (na prática o que acontecerá
        # é que será preciso colocar '_Conta__saldo' e '_Conta__codigo', que não é uma boa prática).
        # Outra solução viável, seria manter os atributos privados com dois underlines,
        # mas criar properties para cada um deles, possibilitando o acesso.
        return self._saldo == other._saldo and self._codigo == other._codigo
        # Esse é o jeito que eu preferiria utilizar (na maioria das vezes), mas às vezes variando
        # entre 'type(o)' e 'isinstance(other, Class)', dependendo da situação.

    def passar_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


if __name__ == '__main__':
    conta1 = ContaPoupanca(542)
    conta2 = ContaCorrente(821)
    print(conta1 == conta2)

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        # Atributos privados = '__nome_do_atributo'
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Getters
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    # Setters
    def set_limite(self, valor):
        self.__limite = valor

    # Métodos gerais
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


if __name__ == "__main__":
    pass

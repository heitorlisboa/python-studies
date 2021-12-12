class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Atributos estáticos
    codigo_banco = '001'
    codigos_bancos = {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @staticmethod
    def teste():
        return Conta.codigo_banco == '001'


if __name__ == '__main__':
    print(Conta.codigo_banco)
    print(Conta.codigos_bancos)
    print(Conta.teste())

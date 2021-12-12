class Conta:
    nome = "Michael"  # Atributo da classe

    def __init__(self, titular):
        self.titular = titular  # Atributo da instância (objeto)

    @classmethod
    def metodo(cls):  # Método da classe
        return "chamando um método"


# Acessando nome da classe
conta = Conta("Erick")
print(conta.__class__.__name__)
# Sem o __class__ não funciona
# print(conta.__name__)
# Porém para atributos e métodos da classe o __class__ não faz diferença alguma
print(conta.__class__.metodo())
print(conta.metodo())

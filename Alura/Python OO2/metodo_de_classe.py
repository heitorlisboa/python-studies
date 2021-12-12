class Funcionario:
    prefixo = 'Instrutor'

    @classmethod  # Método de classe (explicita que o método é da classe e que não será útil
    # para os objetos, mesmo estes podendo utilizá-lo)
    def info(cls):
        return cls.prefixo

    @staticmethod  # Dá pra fazer a mesma coisa usando um método estático
    def info2():
        return Funcionario.prefixo  # Juntamente com o uso do nome da classe para referenciar
    # Porém é mais interessante para heranças utilizar o @classmethod,
    # uma vez que, quando se utiliza um método que explicita a classe que será utilizada
    # e que será utilizado para a criação do objeto, o objeto criado fará parte
    # da classe mãe e não da classe que realmente foi utilizada
    # EXEMPLO: https://www.programiz.com/python-programming/methods/built-in/classmethod
    # (conferir 'Example 3' no final da página)


if __name__ == '__main__':
    funcionario = Funcionario
    funcionario.info()

class Nothing:  # Sempre usar CamelCase em classes
    pass
    """
    Utilizado somente como placeholder, caso a função/classe seja necessária sintaticamente, mas o seu códico não
    """

    @staticmethod  # Necessário pra quando não se usa o primeiro parámetro implícito (self)
    def test():
        print('This is a test!')


# Programa principal
Nothing.test()

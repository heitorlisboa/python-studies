class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property  # Mesmo sendo uma property, não deixa de ser um getter, porém sem a sintaxe 'get_nome'
    def nome(self):
        return self.__nome.title()

    @nome.setter  # O nome no '@' corresponde ao nome da property e não do atributo
    # Mas normalmente se usa o nome da property igual ao do atributo
    def nome(self, nome):  # O nome do parâmetro normalmente é o mesmo nome da property (deixa o nome branco?)
        self.__nome = nome
    # Tanto o '@property' como o '@nome.setter' são chamados de Decorators


if __name__ == "__main__":
    pass

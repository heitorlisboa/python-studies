class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def __str__(self):  # Quando se usa o >> print(o) << se chama esse método
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

    def __repr__(self):  # Quando se usa o >> print(repr(o)) << se chama esse método
        return f"Programa('{self.nome}', {self.ano})"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):  # Quando se usa o >> print(o) << se chama esse método
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

    def __repr__(self):  # Quando se usa o >> print(repr(o)) << se chama esse método
        return f"Filme('{self.nome}', {self.ano}, {self.duracao})"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # Quando se usa o >> print(o) << se chama esse método
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

    def __repr__(self):  # Quando se usa o >> print(repr(o)) << se chama esse método
        return f"Serie('{self.nome}', {self.ano}, {self.temporadas})"


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    vingadores.dar_like()
    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_like()
    atlanta.dar_like()

    print(repr(atlanta))

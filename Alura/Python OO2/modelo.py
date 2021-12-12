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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):  # Quando se usa o >> print(o) << se chama esse método
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # Quando se usa o >> print(o) << se chama esse método
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __getitem__(self, item):  # Torna o objeto iterável
        return self.__programas[item]

    def __len__(self):  # Possibilita o uso do >> len(o) <<
        return len(self.__programas)

    @property
    def listagem(self):
        return self.__programas


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('todo mundo em pânico', 1999, 100)
    demolidor = Serie('demolidor', 2016, 2)
    vingadores.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

    for programa in playlist_fim_de_semana:
        print(programa)

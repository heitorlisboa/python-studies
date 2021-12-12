from abc import ABC  # Abstract Base Classes
from collections.abc import MutableSequence


class Playlist(MutableSequence):
    pass


filmes = Playlist()
# Dá erro pois é necessário, antes, implementar na classe todos os métodos da ABC

from abc import ABCMeta, abstractmethod


class Program(metaclass=ABCMeta):  # Indica que é uma classe abstrata
    @abstractmethod  # Indica que é um método abstrato
    def __str__(self):  # Agora toda classe criada a partir da classe Program,
        pass            # terá que implementar o dunder method __str__

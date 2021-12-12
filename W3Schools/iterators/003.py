# Criando um iterable object e um iterator

class Numbers:  # Iterable object
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1  # Adiciona 1 primeiro e depois retorna, então não começa no 0, mas no 1
        return self.n


# my_iter = Numbers().__iter__()  # Iterator
my_iter = iter(Numbers())  # Iterator

for c in range(0, 10):  # Fazendo iteração
    # print(my_iter.__next__())
    print(next(my_iter))

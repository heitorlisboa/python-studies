class Numbers:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < 20:
            self.n += 1
            return self.n
        else:
            raise StopIteration  # Para a iteração


# Fazendo iteração, dessa vez com iterable object com limite de 20 iterações
for c in iter(Numbers()):
    print(c)

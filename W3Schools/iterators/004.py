from time import sleep


class Numbers:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        sleep(0.5)
        return self.n


# Outra maneira de fazer iteração
for c in iter(Numbers()):
    print(c)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, age=0):  # Feito para herdar o mesmo __init__() e adicionar novos parâmetros
        Person.__init__(self, fname, lname)  # Feito para herdar o mesmo __init__()
        self.age = age  # E adiconar novos atributos

    def print_name(self):  # Sobrepôs-se à função da classe Person
        print(f'Name: {self.firstname} {self.lastname}\n'
              f'Age: {self.age}')


Student('Carlos', 'Eduardo', 17).print_name()

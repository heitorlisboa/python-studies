class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year  # Mesma coisa do 003.py: adição de um novo atributo

    def welcome(self):  # Mesma coisa do 003.py, só que sem sobreposição de função
        print(f'Welcome {self.firstname} {self.lastname} to the class of {self.graduation_year}')


Student('Carlos', 'Eduardo', 2021).welcome()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass  # Quando se usa o pass, a child class vai herdar tudo da parent class


Student('Carlos', 'Eduardo').print_name()

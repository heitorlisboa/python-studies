class Person:  # Sempre usar CamelCase em classes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello, my name is {self.name}!')


person1 = Person('Marcus', 33)
person1.hello()

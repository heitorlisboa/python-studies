my_tuple = ('apple', 'banana', 'cherry')
my_string = 'banana'

"""
sendo 'x' um iterador/iterator (objeto que contêm um número contável de valores):
iter(x) == x.__iter__()
next(x) == x.__next__()
"""

my_iter1 = my_tuple.__iter__()
print(my_iter1.__next__())
print(my_iter1.__next__())
print(my_iter1.__next__())

my_iter2 = iter(my_string)
print(next(my_iter2))
print(next(my_iter2))
print(next(my_iter2))

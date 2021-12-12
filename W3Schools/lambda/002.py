def my_function(n):
    return lambda a: n * a


# O primeiro argumento é da função (n) e o segundo do lambda (a)
print(my_function(5)(8))

my_doubler = my_function(2)
print(my_doubler(5))

my_tripler = my_function(3)
print(my_tripler(5))

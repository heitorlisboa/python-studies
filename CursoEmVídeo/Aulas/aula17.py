from random import randint
num_list = [randint(1, 10), randint(1, 10), randint(1, 10),
            randint(1, 10), randint(1, 10), randint(1, 10)]
num_list2 = num_list[:]
num_list2.append('FIM')
print(num_list)
print(num_list2)

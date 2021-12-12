from random import randint

numbers = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print(f'The numbers drawn are {numbers}')

# Método usando SORTED (lista)
'''print(f'The biggest number is {sorted(numbers)[-1]}\n'
      f'The smallest number is {sorted(numbers)[0]}')'''

# Método usando MAX e MIN
print(f'The biggest number is {max(numbers)}\n'
      f'The smallest number is {min(numbers)}')

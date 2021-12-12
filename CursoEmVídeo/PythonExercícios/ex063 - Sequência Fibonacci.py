# Método do Guanabara de str com minha correção pra quantidade de termos mostrados
"""many = int(input('How many terms do you want for the Fibonacci Sequence? '))
t1 = 0
t2 = 1
count = 2
if many == 0:
    exit()
elif many == 1:
    print(f'{t1}')
elif many == 2:
    print(f'{t1} ➔ {t2}')
elif many >= 3:
    print(f'{t1} ➔ {t2} ➔', end=' ')
    while count < many:
        t3 = t2 + t1
        print(f'{t3} ➔', end=' ')
        count += 1
        t1 = t2
        t2 = t3
    print('END')"""

# Meu método de lista
show = many = int(input('How many terms do you want for the Fibonacci Sequence? '))
fibonacci = [0, 1]
while many > 2:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    many -= 1
print(fibonacci[:show])

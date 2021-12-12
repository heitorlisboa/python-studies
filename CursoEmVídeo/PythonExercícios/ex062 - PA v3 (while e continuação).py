print('{:=^30}'.format('Arithmetic progression'))
ft = int(input('First term: '))
cd = int(input('Common difference: '))
print('The first 10 terms are:')
term = 0
many = 10
more = 1
while more != 0:
    while term != many:
        print(ft + term * cd, end=' ')
        term += 1
    more = int(input('\nHow many more terms do you want to see? (0 = exit) '))
    many += more
print(f'Progression ended with {many} terms.')

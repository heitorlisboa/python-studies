print('{:=^30}'.format('Arithmetic progression'))
ft = int(input('First term: '))
cd = int(input('Common difference: '))
print('The first 10 terms are:')
term = 0
while term != 10:
    print(ft + term * cd, end=' ')
    term += 1

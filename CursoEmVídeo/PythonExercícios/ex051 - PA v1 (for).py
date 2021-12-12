print('{:=^30}'.format('Arithmetic progression'))
ft = int(input('First term: '))
cd = int(input('Common difference: '))
print('The first 10 terms are:')
for c in range(0, 10):
    print(ft + c * cd, end=' ')

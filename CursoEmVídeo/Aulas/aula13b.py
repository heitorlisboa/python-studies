from time import sleep
print('{:=^30}'.format('Cronômetro'))
contagem = int(input('Até quantos segundos quer contar? '))
if contagem > 0:
    for c in range(1, contagem+1):
        sleep(1)
        print(c, end=' ')
    print('\n\033[1;36mTEMPO ACABOU!!!\033[m')
else:
    print('\033[1;31mInsira um tempo VÁLIDO!\033[m')

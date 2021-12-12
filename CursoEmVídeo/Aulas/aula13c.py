soma = 0
quant = int(input('Quantos números quer somar? '))
for c in range(0, quant):
    num = int(input('Digite um valor: '))
    soma = soma + num
print(f'A soma é {soma}')

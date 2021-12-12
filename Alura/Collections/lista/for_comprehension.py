idades = [16, 13, 25, 14, 29]
idades_ano_que_vem = [idade+1 for idade in idades]
print(idades_ano_que_vem)

idades_maiores_que_21 = [idade for idade in idades if idade > 21]
print(idades_maiores_que_21)

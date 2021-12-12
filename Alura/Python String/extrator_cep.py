import re  # Regular Expressions (RegEx)

endereco = 'Rua das Flores 72, Apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

# O padrão é: 5 dígitos + hífen (opcional) + 3 dígitos.
# padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
# O(s) valor(es) dentro de [colchetes] significa os possíveis valores para UM dígito.
# O hífen significa intervalos (funciona tanto para números quanto para letras).
# O número dentro de {chaves} significa o número de vezes que o [colchetes] anterior aparece seguidos.
# O ponto de interrogação significa que é OPCIONAL, ou seja, pode ou não aparecer.

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')  # Já o >>> {0,1} <<< significa que aparece de 0 a 1 vezes.
busca = padrao.search(endereco)  # Retorna um Match.

print(busca)

if busca:
    cep = busca.group()
    print(cep)

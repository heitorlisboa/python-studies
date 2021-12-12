def processamento_lista(lista=[]):  # A definição da função só é executado uma única vez,
    print(len(lista))               # ou seja, a lista se mantem a mesma ao invés de criar uma
    print(lista)                    # lista nova cada vez que executar o comando.
    lista.append(13)


processamento_lista()
processamento_lista()
processamento_lista()

# Uma boa prática para deixar um objeto mutável como opcional, é utilizar o 'none'.
def novo_processamento_lista(lista=None):  # Não é mais problema, pois o valor de NoneType é imutável.
    # A partir daqui, o código será executado toda vez que chamar a função.
    if not lista:  # Ou 'if lista == None:'. Como 'None' retorna falso, as duas maneiras são possíveis.
        lista = []  # Assim, a variável 'lista' recebe uma lista vazia toda vez que a função é chamada.
    print(len(lista))
    print(lista)
    lista.append(13)

novo_processamento_lista()
novo_processamento_lista()
novo_processamento_lista()

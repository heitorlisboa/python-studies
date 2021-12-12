def lista_para_dicionario(lista):
    """
    Se utiliza uma lista com listas de dois termos (duplas) dentro
    para criar um dicionário com o primeiro o primeiro valor da dupla
    sendo a chave do item e o segundo valor da dupla sendo o valor do item

    EXEMPLO:
    lista_para_dicionario([('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)])
    RETORNA {'nome': 'Heitor', 'idade': 17, 'altura': 1.72}
    """
    dicionario = {}
    for dupla in lista:
        dicionario.update({dupla[0]: dupla[1]})
    return dicionario


if __name__ == '__main__':
    teste = lista_para_dicionario([('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)])
    print(teste)

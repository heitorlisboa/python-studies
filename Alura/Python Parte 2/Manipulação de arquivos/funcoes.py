from random import randrange


def entre_linhas(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'{texto:^{tam}}')
    print('-' * tam)


def escolher_palavra_secreta(nome_arquivo='palavras.txt', primeira_linha_valida=1):
    palavras = []

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = randrange(primeira_linha_valida - 1, len(palavras))
    palavra_escolhida = palavras[numero].upper()

    return palavra_escolhida


def inicializa_letras_acertadas(palavra):
    return ['_' for _ in palavra]


def validar_input(letra, lista):
    while True:
        chute = str(input(letra)).strip().upper()
        if 0 < len(chute) < 2 and not chute.isnumeric() and chute not in lista:
            break
        else:
            if not 0 < len(chute) < 2:
                print('\033[1;31mInsira somente uma letra!\033[m')
            if chute.isnumeric():
                print('\033[1;31mInsira uma LETRA!\033[m')
            if chute in lista:
                print('\033[1;31mVocê já utilizou essa letra!\033[m')
    return chute


def marca_chute_correto(chute, resposta, lista):
    for index in range(0, len(resposta)):
        if chute == resposta[index]:
            lista[index] = chute


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def imprime_mensagem_vencedor(resposta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.     ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /       ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(resposta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {resposta}")
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")
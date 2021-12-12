import funcoes as f


def jogar():
    f.entre_linhas('Bem vindo ao jogo da forca!')
    palavra_secreta = f.escolher_palavra_secreta()
    letras_acertadas = f.inicializa_letras_acertadas(palavra_secreta)

    enforcou = acertou = erros = 0
    letras_utilizadas = []

    while not acertou and not enforcou:
        chute = f.validar_input('Digite uma letra: ', letras_utilizadas)

        letras_utilizadas.append(chute)

        if chute in palavra_secreta:
            f.marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            f.desenha_forca(erros)

        enforcou = erros == 7  # Mesma coisa que >> True if erros == 7 else False <<
        acertou = '_' not in letras_acertadas  # Mesma coisa que >> True if '_' not in letras_acertadas else False <<
        print(letras_acertadas)

    if acertou:
        f.imprime_mensagem_vencedor(palavra_secreta)
    else:
        f.imprime_mensagem_perdedor(palavra_secreta)


if __name__ == '__main__':
    jogar()

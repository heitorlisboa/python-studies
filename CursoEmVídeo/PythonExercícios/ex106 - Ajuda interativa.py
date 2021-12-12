from time import sleep


def betweenLines(txt, color='\033[m'):
    var_len = len(txt) + 4
    print(color, end='')
    print('~' * var_len)
    print(f'{txt:^{var_len}}')
    print('~' * var_len)
    print(colors['clear'], end='')


def colouredHelp(txt):
    print(colors['content'], end='')
    help(txt)
    print(colors['clear'], end='')


colors = {
    'title': '\033[1;97;44m',   # Fundo azul e letra branca
    'loading': '\033[97;103m',  # Fundo amarelo claro e branca
    'content': '\033[97;40m',   # Fundo preto e letra branca
    'end': '\033[1;30;107m',    # Fundo branco e letra preta
    'clear': '\033[m'
}


while True:
    betweenLines('PyHELP Assistance System', colors['title'])
    answer = str(input('Enter a function or a package >>> ')).lower()
    if answer == 'quit':
        betweenLines('GOODBYE!', colors['end'])
        break
    betweenLines(f'Accessing \'{answer}\' command guide', colors['loading'])
    sleep(1)
    colouredHelp(answer)
    sleep(0.5)

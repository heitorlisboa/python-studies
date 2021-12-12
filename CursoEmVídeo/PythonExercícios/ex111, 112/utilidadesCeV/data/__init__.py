def inputMoney(txt, auto=False):
    comma = False
    while True:
        answer = value = str(input(txt)).strip()
        if auto and ',' in value:
            comma = True
        value = value.replace(',', '.')
        copy = value.replace('.', '0', 1)
        if copy.isnumeric():
            return float(value) if not comma \
                else str(value.replace('.', ','))
        print('\033[1;31m'
              f'ERROR: "{answer}" is not a valid price!'
              '\033[m')

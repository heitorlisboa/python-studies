def inputInt(txt):
    while True:
        try:
            res = int(input(txt))
        except (ValueError, TypeError):
            print('{}ERROR: please, enter a valid integer.{}'.format(
                '\033[1;31m', '\033[m'
            ))
        except KeyboardInterrupt:  # Não funciona :(
            print('{}The user chose not to enter a value{}'.format(
                '\033[1;31m', '\033[m'
            ))
        else:
            return res


def inputFloat(txt):
    while True:
        try:
            res = float(input(txt))
        except KeyboardInterrupt:  # Não funciona :(
            print('{}The user chose not to enter a value{}'.format(
                '\033[1;31m', '\033[m'
            ))
        except (ValueError, TypeError):
            print('{}ERROR: please, enter a valid real number.{}'.format(
                '\033[1;31m', '\033[m'
            ))
        else:
            return res


def inputWhole(txt):
    while True:
        try:
            res = int(input(txt))
            if res < 0:
                print('{}ERROR: Please enter a positive number.{}'.format(
                    '\033[1;31m', '\033[m'
                ))
                continue
        except (ValueError, TypeError):
            print('{}ERROR: Please enter a valid whole number.{}'.format(
                '\033[1;31m', '\033[m'
            ))
        else:
            return res

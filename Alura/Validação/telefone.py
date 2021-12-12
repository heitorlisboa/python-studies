import re


class TelefoneBr:
    def __init__(self, telefone: str or int, tem_ddi: bool = False):
        telefone = str(telefone)

        if self._valida(telefone, tem_ddi):
            self._tem_ddi = tem_ddi
            self._telefone = self._formata()

        else:
            raise ValueError('Número de telefone inválido!')

    def __str__(self) -> str:
        return self._telefone

    def _valida(self, num: str, tem_ddi: bool = False) -> bool:
        if not tem_ddi:  # Sem DDI
            padrao_telefone = re.compile(
                '(([0-9]{2})|(\([0-9]{2}\)))'
                '[ ]?([9]?[0-9]{4}[-| ]?[0-9]{4})'
            )
            match = padrao_telefone.match(num)

            if match:
                valido = match.group() == num

                if valido:
                    self.num_fatiado = (
                        # Pode conter parênteses
                        self._somente_digitos(match.group(1)),
                        # Pode conter hífen
                        self._somente_digitos(match.group(4))
                    )

        elif tem_ddi:  # Com DDI
            padrao_telefone = re.compile(
                '\+?([0-9]{2,3}) '
                '(([0-9]{2})|(\([0-9]{2}\)))'
                '[ ]?([9]?[0-9]{4}[-| ]?[0-9]{4})'
            )
            match = padrao_telefone.match(num)

            if match:
                valido = match.group() == num

                if valido:
                    self.num_fatiado = (
                        match.group(1),
                        # Pode conter parênteses
                        self._somente_digitos(match.group(2)),
                        # Pode conter hífen
                        self._somente_digitos(match.group(5))
                    )

        return valido

    def _formata(self) -> str:
        if self._tem_ddi:
            # +555 (33) 99999-9999
            num_formatado = '+{} ({}) {}-{}'.format(
                self.num_fatiado[0],
                self.num_fatiado[1],
                self.num_fatiado[2][:-4],
                self.num_fatiado[2][-4:]
            )

        elif not self._tem_ddi:
            # (33) 99999-9999
            num_formatado = '({}) {}-{}'.format(
                self.num_fatiado[0],
                self.num_fatiado[1][:-4],
                self.num_fatiado[1][-4:]
            )

        return num_formatado

    @staticmethod
    def _somente_digitos(num: str) -> str:
        num = ''.join([x for x in num if x.isdigit()])

        return num


if __name__ == '__main__':
    num = '(33) 99999999'
    meu_objeto = TelefoneBr(num, False)
    print(meu_objeto)
    print(meu_objeto.num_fatiado)

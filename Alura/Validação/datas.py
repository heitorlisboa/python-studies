from datetime import datetime, timedelta
from re import template


class Cadastro:
    def __init__(self):
        self._momento_cadastro = datetime.today()

    def momento_cadastro(self, extenso: bool = False) -> str:
        if extenso:
            dias_semana = (
                'Segunda-feira', 'Terça-feira', 'Quarta-feira',
                'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'
            )
            meses = (
                'janeiro', 'fevereiro', 'março',
                'abril', 'maio', 'junho', 'julho',
                'agosto', 'setembro', 'outubro',
                'novembro', 'dezembro'
            )

            temp = self._momento_cadastro

            data_formatada = '{} ({}) de {} de {}'.format(
                dias_semana[temp.weekday()],  # Dia por extenso
                temp.day,                     # Dia em número
                meses[temp.month - 1],        # Mês
                temp.year                     # Ano
            )

        else:
            data_formatada = self._momento_cadastro.strftime('%d/%m/%Y %H:%M')

        print(data_formatada)

    @property
    def tempo_cadastrado(self):
        tempo = (datetime.today() + timedelta(days=30)) - \
            self._momento_cadastro

        return tempo


if __name__ == '__main__':
    meu_cadastro = Cadastro()
    meu_cadastro.momento_cadastro(True)

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:  # Mixin (funcionalidades específicas que não dependem da classe filha)
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):  # Segue a ordem do algorítmo MRO
    pass


class Senior(Alura, Caelum):  # Segue a ordem do algorítmo MRO
    pass


if __name__ == '__main__':
    jose = Junior('José')
    jose.busca_perguntas_sem_resposta()

    lean = Pleno('Lean')
    lean.busca_perguntas_sem_resposta()
    lean.busca_cursos_do_mes()

    lean.mostrar_tarefas()

    print(lean)

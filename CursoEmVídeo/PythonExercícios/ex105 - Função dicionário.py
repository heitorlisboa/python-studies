def grades(*n, sit=False):
    """
    Cria um dicionário com a quantidade, a maior, a menor e a média das notas
    :param n: Notas (pode ser qualquer quantidade)
    :param sit: Se for True, também adiciona ao dicionário a situação; se for False (ou vazio), não adiciona
    :return: Retorna o dicionário criado
    """
    grade = dict()
    grade['total'] = len(n)
    grade['highest'] = max(n)
    grade['lowest'] = min(n)
    mean = sum(n)/len(n)
    grade['mean'] = mean
    if sit:
        if mean < 5:
            grade['situation'] = 'BAD'
        elif mean < 7:
            grade['situation'] = 'MODERATE'
        else:
            grade['situation'] = 'GOOD'
    return grade


answer = grades(5.5, 9.5, 10, 6.5)
print(answer)
help(grades)

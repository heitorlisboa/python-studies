from functools import total_ordering

# Esse decorator cria todas os dunder methods '__lt__', '__le__', '__gt__' e '__ge__'
# a partir do '__eq__' junto com somente um deles (dar preferência ao '__lt__').
@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __str__(self):
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    # Utilizado para ordenação em listas, indicando qual se um objeto é maior que outro
    def __lt__(self, other):
        if self._saldo != other._saldo:  # Se o saldo for diferente
            return self._saldo < other._saldo  # O menor vai ser o que tem menor saldo

        return self._codigo < other._codigo  # Caso contrário, será o menor código

    def depositar(self, valor):
        self._saldo += valor

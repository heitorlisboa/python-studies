from ordenacao_main import ContaSalario
from operator import attrgetter

conta_gui = ContaSalario(413)
conta_gui.depositar(500)
conta_dani = ContaSalario(312)
conta_dani.depositar(1000)
conta_paulo = ContaSalario(57)
conta_paulo.depositar(550)

contas = [conta_gui, conta_dani, conta_paulo]

# Os parâmetros (do 'sorted()') seguintes ao primeiro servirão
# de desempate caso o anterior seja igual entre dois ou mais objetos.
for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)
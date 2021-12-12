from ordenacao_main import ContaSalario

conta_gui = ContaSalario(413)
conta_gui.depositar(500)
conta_dani = ContaSalario(312)
conta_dani.depositar(1000)
conta_paulo = ContaSalario(57)
conta_paulo.depositar(550)

contas = [conta_gui, conta_dani, conta_paulo]

# Possibilitado pela definição do dunder method '__lt__' na classe
# ContaSalario presente no arquivo 'ordenacao_main.py'.
for conta in sorted(contas):
    print(conta)

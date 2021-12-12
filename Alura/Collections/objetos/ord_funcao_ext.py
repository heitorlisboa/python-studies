from ordenacao_main import ContaSalario

conta_gui = ContaSalario(413)
conta_gui.depositar(500)
conta_dani = ContaSalario(312)
conta_dani.depositar(1000)
conta_paulo = ContaSalario(57)
conta_paulo.depositar(550)

contas = [conta_gui, conta_dani, conta_paulo]

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):  # Utilização da função criada como parâmetro.
    print(conta)

# SET (conjunto)
# Um set não apresenta elementos repetidos e não existe ordem de seus elementos.
usuarios_data_science = [13, 54, 23, 46]
usuarios_machine_learning = [13, 92, 23, 35]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

assistiram = set(assistiram)
# O set 'assistiram' não apresenta a mesma ordem dos elementos que aparecem
# nas listas 'usuarios_data_science' e 'usuarios_machine_learning'.

for usuario in assistiram:
    print(usuario)
# Mas a ordem que aparece quando o set foi criado será sempre a mesma depois,
# apesar de não ser possível acessar um index específico.

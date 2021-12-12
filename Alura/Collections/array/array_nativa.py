import array as arr
# É bom evitar o uso do dessa biblioteca ("array puro")

# É necessário passar o tipo de array
numeros = arr.array('d', [1, 3.5])  # Não causa erro.
teste = arr.array('d', [5, 'Guilherme'])  # Causa erro.
# As arrays da biblioteca 'array' permitem limitar que tipo de objeto será recebido por elas 

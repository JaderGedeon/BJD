######################################
# Disciplina: PI 2: Narrativa
# Título: Multiplicar de Itens
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

num_lista = [8,5,1,7]
A = 2
stringLista = ""

for item in num_lista:
    stringLista += str(item)

num_lista = list(str(int(stringLista)*2))
print(num_lista)

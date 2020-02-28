######################################
# Disciplina: PI 2: Narrativa
# Título: Somar Itens
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

ListaA = [8,5,1,7]
ListaB = [1,4,8,5,7]

stringA = ""
stringB = ""

for item in ListaA:
    stringA += str(item)

for item in ListaB:
    stringB += str(item)

Soma = list(str(int(stringA)+int(stringB)))
print(Soma)

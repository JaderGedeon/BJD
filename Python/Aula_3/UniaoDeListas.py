######################################
# Disciplina: PI 2: Narrativa
# Título: Uniao de Itens
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

ListaA = [1,7,4,6,8,2,3]
ListaB = [8,9,3,2,5]

for item in ListaA:
    if item not in ListaB:
        ListaB.append(item)

print(ListaB)
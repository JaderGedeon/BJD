######################################
# Disciplina: PI 2: Narrativa
# Título: Intersecção de Listas
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

ListaA = [1,7,4,6,8,2,3]
ListaB = [8,9,3,2]
ListaAB = []

for item in ListaA:
    if item in ListaB:
        ListaAB.append(item)

print(ListaAB)

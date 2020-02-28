######################################
# Disciplina: PI 2: Narrativa
# Título: Intercalação de Itens
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

ListaA = [1,3,6,7]
ListaB = [2,4,5]

for item in ListaA:
    if item not in ListaB:
        ListaB.append(item)

ListaC = ListaB

for i in range(len(ListaC)):
    for j in range(0,len(ListaC)-i-1):
        if ListaC[j] > ListaC[j+1]:
            ListaC[j], ListaC[j+1] = ListaC[j+1], ListaC[j]

print(ListaC)




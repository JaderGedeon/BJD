######################################
# Disciplina: PI 2: Narrativa
# Título: Inverter Lista
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

contador = 0

Lista = [ 4, 9, 10, 8, 6]
ListaReversa = []

for item in Lista:
    ListaReversa.append(Lista[len(Lista)-contador-1])
    contador+=1

print(ListaReversa)
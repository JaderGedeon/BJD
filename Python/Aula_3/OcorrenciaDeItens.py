######################################
# Disciplina: PI 2: Narrativa
# Título: Ocorrencia De Itens
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

Lista = list(str(input("Digite uma frase: ")))
ListaAuxiliar = []

for item in Lista:
    if item not in ListaAuxiliar:
        ListaAuxiliar.append(item)
        print("%s = %d" % (item, Lista.count(item)))

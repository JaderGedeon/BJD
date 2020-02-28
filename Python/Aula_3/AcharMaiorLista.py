######################################
# Disciplina: PI 2: Narrativa
# Título: Maior na Lista
# Autor: Jader G. O. Rocha
# Data: 27/02/20
######################################

Lista = [ 1.54, 1.98, 2.01, 1.67, 1.79]

maiorNum = Lista[0]

for item in Lista:
    if item > maiorNum:
        maiorNum = item

print("A maior altura é: %.2f" % maiorNum)

######################################
# Disciplina: PI 2: Narrativa
# Título: Palindromo
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def palindromizador(palio):
    testepalio = False
    if palio == palio[::-1]:
        testepalio = True
    return testepalio

palio = str(input("Escreva algo para ver se é palíndromo ou não: "))
print(palindromizador(palio))

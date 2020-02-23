######################################
# Disciplina: PI 2: Narrativa
# Título: Caractere na String
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def acharCaracter(linha,char):
    count = 0
    for i in linha:
        if char == i:
            count +=1
    return count

linha = str(input("Escreva uma frase: "))
char = str(input("Escreva um caractere para ver quantas vezes ele se repete na frase: "))
print("Aparece %d vez(es)" %(acharCaracter(linha,char)))

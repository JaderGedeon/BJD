######################################
# Disciplina: PI 2: Narrativa
# Título: Substituir char na string
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def sumirCaracter(linha,char):

    return linha.replace(char,"")

linha = str(input("Escreva uma frase: "))
char = str(input("Escreva um caractere que irá sumir da frase: "))
print(sumirCaracter(linha,char))

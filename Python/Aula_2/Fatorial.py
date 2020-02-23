######################################
# Disciplina: PI 2: Narrativa
# Título: Fatorial do número
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def fatorial(num):
    try:
        fator = 1
        i = 2
        while i <= num:
            fator = fator*i
            i+=1
        return fator
    except:
        print("\nValores inseridos inválidos")


num = int(input("Informe um número inteiro não negativo: "))
print(fatorial(num))
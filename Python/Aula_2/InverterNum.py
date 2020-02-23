######################################
# Disciplina: PI 2: Narrativa
# Título: Numero invertido
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def inverterNum(num):
    try:
        invertendo = 0
        while num > 0:
            invertendo = int(invertendo * 10 + num % 10)
            num = int(num / 10)
        return invertendo
    except:
        print("\nValores inseridos inválidos")


num = int(input("Informe um número inteiro: "))
print(inverterNum(num))



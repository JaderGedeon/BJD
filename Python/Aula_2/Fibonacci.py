######################################
# Disciplina: PI 2: Narrativa
# Título: Fibonacci
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def fibo(num):
    try:
        totalFibo = 1
        proxNum = 0
        i = 0
        stringFibo = "1"
        while i < num-1:
            totalFibo += proxNum
            proxNum = totalFibo-proxNum
            i+=1
            stringFibo += (", %d"%(totalFibo))
        return stringFibo
    except:
        print("\nValores inseridos inválidos")


num = int(input("Informe até quanto deseja gerar Fibonacci: "))
print(fibo(num))
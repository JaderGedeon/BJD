######################################
# Disciplina: PI 2: Narrativa
# Título: Triangulos
# Autor: Jader G. O. Rocha
# Data: 23/02/20
#####################################

def triangular(tamanhoTriangulo):
    estruturaTriangulo = ""
    larguraTriangulo = 0
    while (0 <= tamanhoTriangulo):
        while larguraTriangulo < tamanhoTriangulo:
            estruturaTriangulo += "%d " %(larguraTriangulo)
            larguraTriangulo +=1
        estruturaTriangulo += "\n"
        larguraTriangulo = 0
        tamanhoTriangulo -=1
    return estruturaTriangulo

tamanhoTriangulo = int(input("Digite o tamanho do triangulo que deseja fazer: "))
print(triangular(tamanhoTriangulo))

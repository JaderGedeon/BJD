######################################
# Disciplina: PI 2: Plataforma
# Título: Ocorrencias em um arquivo
# Autor: Jader G. O. Rocha
# Data: 22/03/20
######################################

arquivoEscrito = "CopiarArquivos_Arquivos/Escrito.txt"

def ocorrenciasArquivo(arquivo):
    arc = open(arquivo, 'r')

    Lista = arc.read()
    ListaAuxiliar = []

    for item in list(Lista):
        if item not in ListaAuxiliar:
            if item != "\n":
                ListaAuxiliar.append(item)
                print("%s = %d" % (item, Lista.count(item)))

    arc.close()

ocorrenciasArquivo(arquivoEscrito)

######################################
# Disciplina: PI 2: Plataforma
# Título: Interseccao de arquivos
# Autor: Jader G. O. Rocha
# Data: 22/03/20
######################################

arquivoUm = "InterseccaoArquivos_Arquivos/ArquivoUm.txt"
arquivoDois = "InterseccaoArquivos_Arquivos/ArquivoDois.txt"

def ocorrenciasArquivo(arquivoUm, arquivoDois):
    arcUm = open(arquivoUm, 'r')
    arcDois = open(arquivoDois, 'r')

    ListaUm = arcUm.read()
    ListaDois = arcDois.read()
    ListaInter = []

    for item in list(ListaUm):
        if item != "\n":
            if item not in ListaInter:
                if item in list(ListaDois):
                    ListaInter.append(item)

    arcUm.close()
    arcDois.close()

    return ListaInter

print(ocorrenciasArquivo(arquivoUm,arquivoDois))

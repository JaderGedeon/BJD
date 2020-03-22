######################################
# Disciplina: PI 2: Plataforma
# Título: Intercalacao de arquivos
# Autor: Jader G. O. Rocha
# Data: 22/03/20
######################################

arquivoUm = "IntercalacaoArquivos_Arquivos/ArquivoUm.txt"
arquivoDois = "IntercalacaoArquivos_Arquivos/ArquivoDois.txt"

def ocorrenciasArquivo(arquivoUm, arquivoDois):
    arcUm = open(arquivoUm, 'r')
    arcDois = open(arquivoDois, 'r')

    listaUm = list(arcUm.read())
    listaDois = list(arcDois.read())

    listaInter = []

    if (len(listaUm) < len(listaDois)):
        for i in range(0, len(listaUm)):
            listaInter.append(listaUm[i])
            listaInter.append(listaDois[i])
    else:
        for i in range(0, len(listaDois)):
            listaInter.append(listaDois[i])
            listaInter.append(listaUm[i])

    arcUm.close()
    arcDois.close()

    return listaInter

print(ocorrenciasArquivo(arquivoUm,arquivoDois))
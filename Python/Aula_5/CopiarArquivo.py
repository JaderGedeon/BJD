######################################
# Disciplina: PI 2: Plataforma
# Título: Copiar Arquivo
# Autor: Jader G. O. Rocha
# Data: 22/03/20
######################################

arquivoEscrito = "CopiarArquivos_Arquivos/Escrito.txt"
arquivoBranco = "CopiarArquivos_Arquivos/Vazio.txt"


def copiarArquivo(arquivoE, arquivoB):
    try:
        fE = open(arquivoE, 'r')
        fB = open(arquivoB, 'w')

        while True:
            texto = fE.readline()
            if texto == "":
                break
            if texto[0] != '#':
                fB.write(texto)

        fE.close()
        fB.close()
    except:
        print("Erro ao ler o arquvo")


copiarArquivo(arquivoEscrito, arquivoBranco)

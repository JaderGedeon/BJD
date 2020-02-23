######################################
# Disciplina: PI 2: Narrativa
# Título: Menu
# Autor: Jader G. O. Rocha
# Data: 20/02/20
#####################################

while True: # =========== MENU ===========

    print("==========[ Menu ]==========\n"
          "( 1 ) > Começar o jogo\n"
          "( 2 ) > Instruções\n"
          "( 3 ) > Sair\n"
          "===================================\n")

    escolhaMenu = int(input("Digite o numero da operacao a fazer: "))

    if escolhaMenu == 1:
        print("\nO jogo ia começar... mas não tem jogo, escolhe outra opção\n")

    elif escolhaMenu == 2:
        print("\nÉ bem simples, é só digitar o númerozinho para escolher a opção :) \n")

    elif escolhaMenu == 3:
        print("\nÓtima escolha")
        break

    else:
        print("\nErro, insira valores válidos \n")
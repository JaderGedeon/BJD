######################################
# Disciplina: PI 2: Narrativa
# Título: Calculadora
# Autor: Jader G. O. Rocha
# Data: 16/02/20
#####################################

import math

def somar(): # ========== FUNÇÃO SOMAR ==============
    try:
        valorSomaUm = int(input("\nDigite o primeiro valor a somar: "))
        valorSomaDois = int(input("Digite o segundo valor a somar: "))
        return ("\nA soma de: %d + %d = %d\n" %(valorSomaUm,valorSomaDois,valorSomaUm+valorSomaDois))
    except:
        print("\nValores inseridos inválidos")

def subtrair(): # ========== FUNÇÃO SUBTRAIR==============
    try:
        valorSubUm = int(input("\nDigite o primeiro valor: "))
        valorSubDois = int(input("Digite o valor a subtrair do primeiro: "))
        return ("\nA subtração de: %d - %d = %d\n" %(valorSubUm,valorSubDois,valorSubUm-valorSubDois))
    except:
        print("\nValores inseridos inválidos")

def multiplicar(): # ========== FUNÇÃO MULTIPLICAR ==============
    try:
        valorMultiUm = int(input("\nDigite o primeiro valor a multiplicar: "))
        valorMultiDois = int(input("Digite o segundo valor a multiplicar: "))
        return ("\nA multiplicação de: %d * %d = %d\n" %(valorMultiUm,valorMultiDois,valorMultiDois*valorMultiUm))
    except:
        print("\nValores inseridos inválidos")

def dividir(): # ========== FUNÇÃO DIVIDIR ==============
    try:
        valorDivUm = int(input("\nDigite o primeiro valor: "))
        valorDivDois = int(input("Digite em quantas vezes dividirá o primeiro valor: "))
        return ("\nA divisão de: %d / %d = %d\n" %(valorDivUm,valorDivDois,valorDivUm/valorDivDois))
    except:
        print("\nValores inseridos inválidos")

def raiz(): # ========== FUNÇÃO RAIZ QUADRADA ==============
    try:
        valorRaiz = int(input("\nDigite um valor para saber sua raiz quadrada: "))
        return ("\nA raiz quadrada de: %d = %d\n" %(valorRaiz,math.sqrt(valorRaiz)))
    except:
        print("\nValores inseridos inválidos")



while True: # ================================ MENU =======================================

    print("==========[ CALCULADORA ]==========\n"
          "( 1 ) > Somar\n"
          "( 2 ) > Substrair\n"
          "( 3 ) > Multiplicar\n"
          "( 4 ) > Dividir (Divisão simples)\n"
          "( 5 ) > Raiz Quadrada\n"
          "( 9 ) > Desligar Calculadora\n"
          "===================================")

    operacao = int(input("Digite o numero da operacao a fazer: "))

    if operacao == 1: # SOMA
        print(somar())
    elif operacao == 2: # SUBSTRACAO
        print(subtrair())
    elif operacao == 3: # MULTIPLICACAO
        print(multiplicar())
    elif operacao == 4: # DIVISAO
        print(dividir())
    elif operacao == 5: # RAIZ
        print(raiz())
    elif operacao == 9: # SAIR
        break
    else: # ERRO DE LEITURA
        print("\n Erro, insira valores válidos \n")
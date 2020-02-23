######################################
# Disciplina: PI 2: Narrativa
# Título: FichaRPG
# Autor: Jader G. O. Rocha
# Data: 20/02/20
######################################

import random

atributosPersonagem = {'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0, 'Sabedoria': 0, 'Carisma': 0}

atributosBonusPersonagem = {'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0, 'Sabedoria': 0, 'Carisma': 0}

#MENU

print("Olá, aventureiro(a), tudo bem com você?\n"
      "Que tal começarmos nossa jornada nesse mundo?\n")

nomePersonagem = str(input("Mas antes... Qual é seu nome?\n"))

print("\nCerto... Já vi nomes piores.\n"  # === NARRADOR ===
      "E pelo visto não é só o nome que é feio...\n\n"
      "( 1 ) - Humano\n"
      "( 2 ) - Elfo\n"
      "( 3 ) - Anão\n"
      "( 4 ) - Orc\n")

inputRaca = int(input("Você é o que?\n"))

if inputRaca == 1:
    racaPersonagem = "Humano"
elif inputRaca == 2:
    racaPersonagem = "Elfo"
elif inputRaca == 3:
    racaPersonagem = "Anão"
elif inputRaca == 4:
    racaPersonagem = "Orc"



print("\nÉ... realmente... não tem nada que presta não... COF! COF!\n"  # === NARRADOR ===
      "Continuando... Numa pergunta mais pessoal...\n\n"
      "( 1 ) - Menino\n"
      "( 2 ) - Menina\n")

inputGenero = int(input("Qual é seu gênero?\n"))

if inputGenero == 1:
    generoPersonagem = "Homem"
elif inputGenero == 2:
    generoPersonagem= "Mulher"




print("\nJá estou quase desistindo... Você parece um caso perdido...\n"  # === NARRADOR ===
      "Mas deixando a beleza de lado, vamo ver seus atributos\n"
      "Irei aleatorizá-los, espero que goste do resultado...")

for atributo in atributosPersonagem:
    atributosPersonagem[atributo] = random.randint(1, 20)


print("Antes de ver seus atributos, que tal escolher sua classe?\n" # === NARRADOR ===
      "Existem essas opções de vocação para decidir, escolha com sabedoria!\n\n"
      "( 1 ) - Guerreiro: (+1 de Força e +2 de Constituição)\n"
      "( 2 ) - Arqueiro: (+2 de Destreza e +1 Inteligência)\n"
      "( 3 ) - Mago: (+2 de Sabedoria e +1 de Inteligência)\n"
      "( 4 ) - Sacerdote (+1 de Sabedoria e +2 de Carisma)\n"
      )

inputClasse = int(input("O que você faz da vida?\n"))

if inputClasse == 1:
    classePersonagem = str("Guerreiro")
    atributosBonusPersonagem['Força'] += 1
    atributosBonusPersonagem['Constituição'] += 2

elif inputClasse == 2:
    classePersonagem = str("Arqueiro")
    atributosBonusPersonagem['Destreza'] += 2
    atributosBonusPersonagem['Inteligência'] += 1

elif inputClasse == 3:
    classePersonagem = str("Mago")
    atributosBonusPersonagem['Sabedoria'] += 2
    atributosBonusPersonagem['Inteligência'] += 1

elif inputClasse == 4:
    classePersonagem = str("Sacerdote")
    atributosBonusPersonagem['Sabedoria'] += 1
    atributosBonusPersonagem['Carisma'] += 2

print("\n\nAventureiro, sua ficha ficou assim\n\n")

print("==========[ Ficha RPG D&D 5 ]==========\n\n"  # === NARRADOR ===
      "Nome:",nomePersonagem,"\n"
      "Raça:",racaPersonagem,"\n"
      "Gênero:", generoPersonagem, "\n"
      "Classe:", classePersonagem, "\n\n"
                                    
      "Força:", atributosPersonagem['Força'], "(+",atributosBonusPersonagem['Força'],")\n"
      "Destreza:", atributosPersonagem['Destreza'], "(+",atributosBonusPersonagem['Destreza'],")\n"
      "Constituição:", atributosPersonagem['Constituição'], "(+",atributosBonusPersonagem['Constituição'],")\n"
      "Inteligência:",atributosPersonagem['Inteligência'], "(+",atributosBonusPersonagem['Inteligência'],")\n"
      "Sabedoria:", atributosPersonagem['Sabedoria'], "(+",atributosBonusPersonagem['Sabedoria'],")\n"
      "Carisma:",atributosPersonagem['Carisma'], "(+",atributosBonusPersonagem['Carisma'],")\n"
      "=====================================\n\n"
      )









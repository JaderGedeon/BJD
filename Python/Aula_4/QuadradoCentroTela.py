######################################
# Disciplina: PI 2: Plataforma
# Título: Quadrado Centro da Tela
# Autor: Jader G. O. Rocha
# Data: 05/03/20
######################################

import pygame

xTela = int(input("Digite a largura ( <-----> ) da janela:"))
yTela = int(input("Digite a altura ( ║ ) da janela:"))

pygame.init()
screen = pygame.display.set_mode((xTela,yTela))
pygame.display.set_caption("Quadrado centro da tela")
JogoAtivo = True

# Definição quadrado

CordsBloco = pygame.Rect((xTela-100)/2,(yTela-200)/2,100,200)
LARANJA = (255,165,0)
Bloco = pygame.draw.rect(screen,LARANJA,CordsBloco)

while JogoAtivo:

    for evento in pygame.event.get():
        #print(evento)

        if evento.type == pygame.QUIT:
            JogoAtivo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                JogoAtivo = False
    pygame.display.flip()


######################################
# Disciplina: PI 2: Plataforma
# Título: Quadrado no Canto Inferior
# Autor: Jader G. O. Rocha
# Data: 05/03/20
######################################

import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Quadrado no canto inferior")
JogoAtivo = True

# Tamanho da tela
xTela = screen.get_width()
yTela = screen.get_height()
# Definição quadrado

CordsBloco = pygame.Rect(xTela-100,yTela-200,100,200)
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


######################################
# Disciplina: PI 2: Narrativa
# Título: Ola Pygames
# Autor: Jader G. O. Rocha
# Data: 05/03/20
######################################

import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Ola Mundo")
JogoAtivo = True
while JogoAtivo:
    # trata os eventos da fila de eventos
    for evento in pygame.event.get():
        print(evento)
        #verifica se o evento que veio eh
		  #para fechar a janela
        if evento.type == pygame.QUIT:
            JogoAtivo = False
        if evento.type == pygame.KEYDOWN:
            print('uma tecla foi pressionada')
            if evento.key == pygame.K_ESCAPE:
                JogoAtivo = False
            if evento.key == pygame.K_q:
                print('FOI FOI')
                bloco = pygame.Rect(200,100,100,100)
                VERDE = (0,255,0)
                oi = pygame.draw.rect(screen,VERDE,bloco)
            if evento.key == pygame.K_w:
                print('FOI FOI')
                blocoz = pygame.Rect(0,0,50,50)
                blocoz.center = bloco.center
                AZUL = (0,0,255)
                pygame.draw.rect(screen, AZUL, blocoz)
                print(blocoz)
        if evento.type == pygame.KEYUP:
            print('uma tecla foi liberada')
    pygame.display.flip()


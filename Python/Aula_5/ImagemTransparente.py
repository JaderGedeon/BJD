######################################
# Disciplina: PI 2: Plataforma
# Título: Tudo de imagens em um
# Autor: Jader G. O. Rocha
# Data: 22/03/20
######################################

import pygame


# Função Clisão

xTela = 600
yTela = 400

screen = pygame.display.set_mode((xTela, yTela))
screen.fill((220, 220, 220))

pygame.init()

pygame.display.set_caption("Quadrado Movel")
JogoAtivo = True

tempo = 0
clock = pygame.time.Clock()

# Definição quadrado
imagemX = (yTela-205)/2
aceleracao = 1

recorteX = 65
margemX = 0

imagem = pygame.image.load("Imagens/Desenho.bmp")
transColor = (255, 0, 255)
imagem.set_colorkey(transColor)

screen.blit(imagem, (int((xTela+130)/2), int(imagemX)),(margemX, 0, recorteX, 205))

while JogoAtivo:

    dt = clock.tick()
    tempo += dt

    if tempo > 150:
        if margemX > 259:
            margemX = 0

        screen.fill((220, 220, 220))
        screen.blit(imagem, (int((xTela-65)/2), int(imagemX)),(margemX, 0, recorteX, 205))

        imagemX += int(1 * aceleracao)
        aceleracao += 0.1

        margemX += 65

        tempo = 0

    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:
            JogoAtivo = False

    pygame.display.flip()



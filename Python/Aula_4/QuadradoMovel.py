######################################
# Disciplina: PI 2: Plataforma
# Título: Quadrado Movivel
# Autor: Jader G. O. Rocha
# Data: 05/03/20
######################################

import pygame

# Função Mover
def movimento(objeto,x,y):
    objeto = (objeto.left+x,objeto.top+y,50,50)
    return objeto

# Função Clisão

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Quadrado Movel")
JogoAtivo = True

# Definição quadrado

CordsBloco = pygame.Rect(0,0,50,50)
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
            if evento.key == pygame.K_DOWN:
                screen.fill((0, 0, 0))
                CordsBloco = pygame.Rect(movimento(CordsBloco,10,10))
                Bloco = pygame.draw.rect(screen,LARANJA,CordsBloco)
                print("Foi")
    pygame.display.flip()
    
# Para fazer com que o quadrado colida com a tela basta verificar a posição dele em relação à tela.

# Para fazer com que o quadrado ande com a tecla pressionada basta adicionar um boolean para verificar se a tecla foi pressionada e ainda não foi solta.


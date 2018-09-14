import pygame
from funciones import *
import math
from dibujos import *
ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Traslacion")
    reloj = pygame.time.Clock()
    pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
    pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
    punto1 = [0,0]
    punto2 = [0,0]
    x = 0
    fin = True
    while fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = False

        #r = int(140*math.sin(0.25*math.radians(x)))
        pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, polares(r, x)), 1)
        x += 1



        #pantalla.fill(NEGRO)


        #pygame.draw.line(pantalla, ROJO, trascartesiano(CENTRO, punto2), trascartesiano(CENTRO, punto1), 5)
        #pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
        #pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
        pygame.display.flip()
        reloj.tick(100)


    pygame.quit()

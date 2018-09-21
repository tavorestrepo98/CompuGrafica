import pygame
from funciones import *
from math import *
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
    pygame.display.set_caption("POLARES")
    reloj = pygame.time.Clock()
    pygame.draw.line(pantalla, BLANCO, (CENTRO[0], 0), (CENTRO[0], alto), 4)
    pygame.draw.line(pantalla, BLANCO, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
    x = 0
    fin = True
    while fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = False

        #r = 140*sin(4*radians(x))
        r=int(280*cos(radians(3*x)))#flor n petalos
        r2=int(280*sin(radians(3*x-78)))
        #r = 200#circunferencia
        #r = 1 + 0.1*x#espiral de arquimedes
        #r = int(60/(1 + 0.8*cos(radians(x))))#elipse
        #r = 30/(1 + 1.5*cos(radians(x)))  #hiperbola
        #r = 100 + 100*cos(radians(x))#cardioide
        #r = 50 + 80*cos(radians(x))#caracol con lazo interno
        pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, polares(r, x)), 2)
        pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, polares(r2, x)), 2)


        x += 0.12



        #pantalla.fill(NEGRO)


        #pygame.draw.line(pantalla, ROJO, trascartesiano(CENTRO, punto2), trascartesiano(CENTRO, punto1), 5)
        #pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
        #pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
        pygame.display.flip()
        reloj.tick(2000)


    pygame.quit()

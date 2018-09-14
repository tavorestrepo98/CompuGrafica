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
    pygame.display.set_caption("Traslacion")
    reloj = pygame.time.Clock()
    pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
    pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
    punto1 = [0,0]
    punto2 = [0,0]
    angulo = 2
    fin = True
    while fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    punto1 = list(pygame.mouse.get_pos())
                    p1 = list(pygame.mouse.get_pos())
                    punto1 = pant_cart2(CENTRO, punto1)
                    p1 = pant_cart2(CENTRO, p1)
                elif event.key == pygame.K_b:
                    punto2 = list(pygame.mouse.get_pos())
                    punto2 = pant_cart2(CENTRO, punto2)
                elif event.key == pygame.K_LEFT:
                    punto1 = rot_punto(p1, punto1)
                    punto2 = rot_punto(p1, punto2)
                    punto1 = rotacion(punto1, pi/100)
                    punto2 = rotacion(punto2, pi/100)
                    punto2 = tras_original(p1, punto2)
                    punto1 = tras_original(p1, punto1)


        #pantalla.fill(NEGRO)
        #pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, pant_cart2(CENTRO, punto1)), 4)

        pygame.draw.line(pantalla, ROJO, trascartesiano(CENTRO, punto2), trascartesiano(CENTRO, punto1), 5)
        pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
        pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
        pygame.display.flip()
        reloj.tick(200)


    pygame.quit()

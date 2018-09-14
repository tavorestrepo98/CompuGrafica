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
    p1 = [150, 100]
    p2 = [400, 100]
    p11 = [0, 0]
    p22 = [0, 0]
    p33 = [0, 0]
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Gustavo")
    pygame.draw.line(pantalla, BLANCO, (CENTRO[0], 0), (CENTRO[0], alto), 4)
    pygame.draw.line(pantalla, BLANCO, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
    pygame.display.flip()
    fin = False
    band = 0
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p11 = pant_cart2(CENTRO, list(pygame.mouse.get_pos()))
                elif event.key == pygame.K_b:
                    p22 = pant_cart2(CENTRO, list(pygame.mouse.get_pos()))
                elif event.key == pygame.K_c:
                    p33 = pant_cart2(CENTRO, list(pygame.mouse.get_pos()))
                elif event.key == pygame.K_SPACE:
                    band = 1
                elif event.key == pygame.K_n:

                    p11 = escalamiento(p11, [2,2])
                    p22 = escalamiento(p22, [2,2])
                    p33 = escalamiento(p33, [2,2])
                elif event.key == pygame.K_LEFT:
                    p11 = tras_centro(p11, p11)
                    p22 = tras_centro(p11, p22)
                    p33 = tras_centro(p11, p22)

                elif event.key == pygame.K_RIGHT:
                    p11 = tras_original(p11, p11)
                    p22 = tras_original(p11, p22)
                    p33 = tras_original(p11, p22)

        pantalla.fill(NEGRO)
        pygame.draw.polygon(pantalla, VERDE, [trascartesiano(CENTRO,p11), trascartesiano(CENTRO, p22), trascartesiano(CENTRO, p33)], 2)
        if band == 1:
            pygame.draw.circle(pantalla, ROJO, trascartesiano(CENTRO, [int(p11[0]), int(p11[1])]), 4)

        pygame.draw.line(pantalla, BLANCO, (CENTRO[0], 0), (CENTRO[0], alto), 3)
        pygame.draw.line(pantalla, BLANCO, (0, CENTRO[1]), (ancho, CENTRO[1]), 3)
        pygame.display.flip()
        reloj.tick(200)
    pygame.quit()

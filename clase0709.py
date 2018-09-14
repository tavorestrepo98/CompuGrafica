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
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Holaaa")
    tux = pygame.image.load("fondo.png")
    i = 0
    j = 0
    pantalla.blit(tux, [i, j])
    pygame.display.flip()
    reloj = pygame.time.Clock()
    posicionamiento = list(tux.get_rect())
    alto_imagen = posicionamiento[3]
    ancho_imagen = posicionamiento[2]
    hecho = True
    while hecho:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hecho = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    i += 10
                elif event.key == pygame.K_LEFT:
                    i -= 10
                elif event.key == pygame.K_UP:
                    j-= 10
                elif event.key == pygame.K_DOWN:
                    j += 10




        pantalla.fill(NEGRO)
        i -= 3
        pantalla.blit(tux, [i, j])
        pygame.display.flip()
        reloj.tick(200)

    pygame.quit()

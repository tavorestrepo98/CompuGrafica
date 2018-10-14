import pygame
from funciones import *
from math import *
from random import *
from personajes import*

def recortar(imagen, alto, ancho):
    l1 = []
    l2 = []
    for i in range(0, alto):
        for j in range(0, ancho):
            cuadro = imagen.subsurface(j*32, 32*i, 32, 32)
            l2.append(cuadro)
        l1.append(l2)
        l2 = []
    return l1


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
    pygame.display.set_caption("LABERINTO")
    pygame.display.flip()
    ter = pygame.image.load("terrenogen.png")
    print ter.get_rect()
    animal = pygame.image.load("animals.png")
    m1 = recortar(ter, 12, 32)
    a1 = recortar(animal, 8, 12)
    i = 6
    reloj = pygame.time.Clock()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pantalla.fill(NEGRO)
                    pantalla.blit(pygame.transform.scale(a1[0][i], [100, 100]), [(ancho/2)-41, (alto/2)-72])
                    if i<8:
                        i+=1
                    else:
                        i = 6
                    pygame.display.flip()
                if event.key == pygame.K_UP:
                    pantalla.fill(NEGRO)
                    pantalla.blit(pygame.transform.scale(a1[3][i], [100, 100]), [(ancho/2)-41, (alto/2)-72])
                    pygame.display.flip()
                    if i<8:
                        i+=1
                    else:
                        i = 6
                if event.key == pygame.K_RIGHT:
                    pantalla.fill(NEGRO)
                    pantalla.blit(pygame.transform.scale(a1[2][i], [100, 100]), [(ancho/2)-41, (alto/2)-72])
                    pygame.display.flip()
                    if i<8:
                        i+=1
                    else:
                        i = 6
                if event.key == pygame.K_LEFT:
                    pantalla.fill(NEGRO)
                    pantalla.blit(pygame.transform.scale(a1[1][i], [100, 100]), [(ancho/2)-41, (alto/2)-72])
                    pygame.display.flip()
                    if i<8:
                        i+=1
                    else:
                        i = 6
            elif event.type == pygame.KEYUP:
                pantalla.fill(NEGRO)



        reloj.tick(50)

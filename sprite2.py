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
            cuadro = imagen.subsurface(j*70, 80*i, 70, 80)
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
    pygame.display.set_caption("KEN")
    img_ken = pygame.image.load('ken.png')
    m = recortar(img_ken, 10, 7)
    lim = [3, 3, 2, 4, 1, 3, 4, 4, 6, 0]
    accion = 0
    con = 0

    reloj = pygame.time.Clock()
    i = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    accion = 2
                if event.key == pygame.K_UP:
                    accion = 8
            elif event.type == pygame.KEYUP:
                pantalla.fill(NEGRO)
        pantalla.fill(NEGRO)
        pantalla.blit(m[accion][con], [0, 0])
        con +=1
        if con>lim[accion]:
            con=0
        pygame.display.flip()
        reloj.tick(9)

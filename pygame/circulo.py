# -*- coding: utf-8 -*-
import pygame
import sys

from pygame.locals import *

pygame.init()
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
    ventana = pygame.display.set_mode((1310,705))
    pygame.display.set_caption("Hola Gonorrea")
    color = pygame.Color(70, 80, 150)
    ventana.fill(NEGRO)
    #pygame.draw.rect(ventana, NEGRO, [30, 60,412, 130])
    #pygame.draw.line(ventana, BLANCO, (300, 300), (100, 100), 3)
   
    hecho = True
    i = -350
    #j = 0
   
    while hecho:
        if i > 930:
            i = -313
    	ventana.fill(NEGRO)
    	for event in pygame.event.get():
    		if event.type == QUIT:
    			hecho = False
    			print "El usuario solicitó salir."
    		elif event.type == KEYDOWN:
    			print "El usuario presionó una tecla"
    		elif event.type == KEYUP:
    			print "El usuario soltó una tecla"
    		elif event.type == MOUSEBUTTONDOWN:
    			print "El usuario presionó un botón del ratón"
    		elif event.type == MOUSEBUTTONUP:
    			print "El usuario soltó un botón del ratón"
        #pygame.draw.line(ventana, BLANCO, (0, 0), (i, j), 3)

        pygame.draw.circle(ventana, BLANCO, (655, i), 7)
        i = i+1
        print i
        #j = j+ 0.27
    	pygame.display.update()
        pygame.display.flip()


    pygame.quit()
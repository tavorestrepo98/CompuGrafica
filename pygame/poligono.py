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
    
   
    hecho = True
    i = -120
    i2 = 1310
    j = 0
   
    while hecho:
    
        if i > 1300:
            i = -120
            
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

        pygame.draw.polygon(ventana, BLANCO, ((i+80, 70), (i+34, 118), (i+56, 160), (i+267, 497)))
        
        i = i+0.5
        i2 = i2 - 0.5
        j = j+ 0.27
    	pygame.display.update()
        pygame.display.flip()


    pygame.quit()

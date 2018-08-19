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
   
    while hecho:
    	
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
    	fuente = pygame.font.Font(None, 55)
    	texto = fuente.render("Gustavo Restrepo", True, VERDE)
    	ventana.blit(texto, (463, 352))
        
    	pygame.display.update()
        pygame.display.flip()


    pygame.quit()
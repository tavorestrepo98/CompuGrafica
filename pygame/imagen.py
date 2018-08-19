# -*- coding: utf-8 -*-
import pygame
import sys
from pygame.locals import *
from random import *

pygame.init()
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
    ventana = pygame.display.set_mode((1310,705))
    pygame.display.set_caption("Bart")
    color = pygame.Color(70, 80, 150)
    ventana.fill(BLANCO)
    
    hecho = True
    my_imagen = pygame.image.load("imagenes/bart.gif")
    i = -5
    x = 590
    y = 300
   
    while hecho:

    	ventana.fill(BLANCO)
        ventana.blit(my_imagen, (x,y))
    	for event in pygame.event.get():
    		if event.type == QUIT:
    			hecho = False
    			print "El usuario solicitó salir."
    		elif event.type == pygame.KEYDOWN:
    			if event.type == K_SPACE:
    				print "Tecla izquierda"
    				x = x-1
    			elif event.type == K_RIGHT:
    				x = x+1
    			elif event.type == K_UP:
    				y = y-1
    			elif event.type == K_DOWN:
    				y = y+1
    				
    	pygame.display.update()
        #pygame.display.flip()
        
        #print i


    pygame.quit()

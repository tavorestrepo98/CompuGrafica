import pygame
from funciones import *
from math import *
ancho = 1352
alto = 710
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
	p1 = [200, 450]
	lp2 = [200, 244]
	lp3 = [400, 244]
	cont1 = 0
	cont2 = 0
	cont3 = 0
	cont4 = 0
	cont5 = 0
	cont6 = 0
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Triangulo")
	pygame.draw.line(pantalla, VERDE, p1, lp2, 4)
	pygame.draw.line(pantalla, VERDE, p1, lp3, 4)
	pygame.draw.line(pantalla, VERDE, lp2, lp3, 4)
	pygame.display.flip()
	cont = 0
	fin = False
	reloj = pygame.time.Clock()
	i = 1
	j = 1
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True					
		lp2 = traslacion(lp2, [0, -1])
		lp3 = traslacion(lp3, [0, -1])
		pantalla.fill(NEGRO)
		pygame.draw.line(pantalla, VERDE, [200, 450], [200, 244], 4)
		pygame.draw.line(pantalla, VERDE, [200, 450], [400, 244], 4)
		pygame.draw.line(pantalla, VERDE, lp2, lp3, 4)



		pygame.display.flip()				
	pygame.quit()
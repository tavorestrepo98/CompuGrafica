import pygame
from funciones import *
from math import *
ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
	p1 = trascartesiano(CENTRO, [200, 290])
	p2 = trascartesiano(CENTRO, [200, 44])
	p3 = trascartesiano(CENTRO, [400, 44])
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Triangulo")
	pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
	pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
	pygame.display.flip()
	cont = 0
	fin = False
	reloj = pygame.time.Clock()
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			elif event.type == pygame.KEYDOWN:
				#angulo = input("Cuantos grados quiere rotarlo? "				
				pantalla.fill(NEGRO)
				pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
				pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
				pygame.draw.polygon(pantalla, VERDE, [p1, p2, p3], 5)
				#print "Pulso una tecla"
				pygame.display.flip()

			#pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, [0, 0]), 130, 5)


		pygame.display.flip()				
	pygame.quit()
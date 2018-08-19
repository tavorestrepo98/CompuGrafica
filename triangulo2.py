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
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Triangulo")
	#pygame.draw.polygon(pantalla, VERDE, [[100, 300], [100, 54], [300, 54]], 5)
	p1 = [200, 290]
	p2 = [200, 44]
	p3 = [400, 44]
	#pygame.display.flip()
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			elif event.type == pygame.KEYDOWN:
				#angulo = input("Cuantos grados quiere rotarlo? ")
				angulo = pi/18
				p1 = rotacion(p1, angulo)
				p2 = rotacion(p2, angulo)
				p3 = rotacion(p3, angulo)
				#pantalla.fill(NEGRO)
				pygame.draw.polygon(pantalla, VERDE, [p1, p2, p3], 5)
				#print "Pulso una tecla"
				pygame.display.flip()
	pygame.quit()
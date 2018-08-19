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
	p1 = [200, 250]
	p2 = [200, 44]
	p3 = [400, 44]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Triangulo")
	cont = 0
	fin = False
	reloj = pygame.time.Clock()
	while not fin:
		'''
		if p1[0] > 1350:
			p1 = [200, 290]
			p2 = [200, 44]
			p3 = [400, 44]
			'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					band1 = True
					while band1:
						p1 = traslacion(p1, [-5, 0])
						p2 = traslacion(p2, [-5, 0])
						p3 = traslacion(p3, [-5, 0])
						pygame.draw.polygon(pantalla, VERDE, [p1, p2, p3], 4)
						if event.type == pygame.KEYDOWN:
							band1 = False

					
				elif event.key == pygame.K_RIGHT:
					p1 = traslacion(p1, [5, 0])
					p2 = traslacion(p2, [5, 0])
					p3 = traslacion(p3, [5, 0])
				elif event.key == pygame.K_UP:
					p1 = traslacion(p1, [0, -5])
					p2 = traslacion(p2, [0, -5])
					p3 = traslacion(p3, [0, -5])
				elif event.key == pygame.K_DOWN:
					p1 = traslacion(p1, [0, 5])
					p2 = traslacion(p2, [0, 5])
					p3 = traslacion(p3, [0, 5])
			#elif event.type == pygame.KEYDOWN:
		#pygame.draw.line(pantalla, VERDE, (100, 100), (100+2*cont, 100))
		
		pantalla.fill(NEGRO)
		pygame.draw.polygon(pantalla, VERDE, [p1, p2, p3], 4)
		pygame.display.flip()
		cont = cont + 1
		reloj.tick(30)
	pygame.quit()
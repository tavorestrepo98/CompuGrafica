import pygame
from funciones import *
from math import *
from dibujos import *
ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':

	p1 = [0, 0]
	p2 = [0, 0]
	p3 = [0, 0]
	p4 = [0, 0]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Triangulo")
	#pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
	#pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
	pygame.display.flip()
	cont = 0
	fin = False
	reloj = pygame.time.Clock()
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					p1 = list(pygame.mouse.get_pos())

				elif event.key == pygame.K_b:
					p2 = list(pygame.mouse.get_pos())

				elif event.key == pygame.K_c:
					p3 = list(pygame.mouse.get_pos())

				elif event.key == pygame.K_d:
					p4 = list(pygame.mouse.get_pos())
				elif event.key == pygame.K_LEFT:
					p1 = traslacion(p1, [-3, 0])
					p2 = traslacion(p2, [-3, 0])
					p3 = traslacion(p3, [-3, 0])
					p4 = traslacion(p4, [-3, 0])
				elif event.key == pygame.K_RIGHT:
					p1 = traslacion(p1, [3, 0])
					p2 = traslacion(p2, [3, 0])
					p3 = traslacion(p3, [3, 0])
					p4 = traslacion(p4, [3, 0])
				elif event.key == pygame.K_UP:
					p1 = traslacion(p1, [0, -3])
					p2 = traslacion(p2, [0, -3])
					p3 = traslacion(p3, [0, -3])
					p4 = traslacion(p4, [0, -3])
				elif event.key == pygame.K_DOWN:
					p1 = traslacion(p1, [0, 3])
					p2 = traslacion(p2, [0, 3])
					p3 = traslacion(p3, [0, 3])
					p4 = traslacion(p4, [0, 3])


			pantalla.fill(NEGRO)
			#pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
			#pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
			pygame.draw.line(pantalla, ROJO, p1, p2, 2)
			pygame.draw.line(pantalla, ROJO, p3, p4, 2)
			pygame.display.flip()

		
		
		pygame.display.flip()
		reloj.tick(100)

	pygame.quit()

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

	p1 =  [200, 290]
	p2 = [200, 44]
	p3 = [400, 44]
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
				pantalla.fill(NEGRO)
				pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
				pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
				pygame.draw.circle(pantalla, VERDE, [int(trascartesiano(CENTRO, p1)[0]), int(trascartesiano(CENTRO, p1)[1])], 20)
				
				#pygame.draw.polygon(pantalla, VERDE, [trascartesiano(CENTRO, p1), trascartesiano(CENTRO, p2), trascartesiano(CENTRO, p3)], 5)
				p1 = rotacion(p1, pi/30)
				p2 = rotacion(p2, pi/30)
				p3 = rotacion(p3, pi/30)
				#rectangulo(pantalla, (trascartesiano(CENTRO, [220, 230])[0],trascartesiano(CENTRO, [220, 230])[1], 300, 200))

				pygame.display.flip()

			#pygame.draw.circle(pantalla, AZUL, trascartesiano(CENTRO, [0, 0]), 130, 5)
		reloj.tick(200)

	pygame.quit()

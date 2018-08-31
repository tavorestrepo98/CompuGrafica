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
	p1 = [150, 100]
	p2 = [400, 100]
	p11 = [0, 0]
	p22 = [0, 0]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Gustavo")
	pygame.draw.line(pantalla, BLANCO, (CENTRO[0], 0), (CENTRO[0], alto), 4)
	pygame.draw.line(pantalla, BLANCO, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
	pygame.display.flip()
	fin = False
	reloj = pygame.time.Clock()
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					p11 = pant_cart(CENTRO, list(pygame.mouse.get_pos()))
				elif event.key == pygame.K_b:
					p22 = pant_cart(CENTRO, list(pygame.mouse.get_pos()))
				elif event.key == pygame.K_SPACE:
					p11 = rotacion(p11, pi/30)
					p22 = rotacion(p22, pi/30)

		
		pygame.draw.line(pantalla, VERDE, p11, p22, 4)
		pygame.draw.line(pantalla, BLANCO, (CENTRO[0], 0), (CENTRO[0], alto), 3)
		pygame.draw.line(pantalla, BLANCO, (0, CENTRO[1]), (ancho, CENTRO[1]), 3)
		pygame.display.flip()
				
		reloj.tick(200)

	pygame.quit()


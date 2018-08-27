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
	l1 = 0
	l2 = 0
	l3 = 0
	perimetro = 0
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
				if event.key == pygame.K_a:
					p1 = list(pygame.mouse.get_pos())
					#p1 = trascartesiano(CENTRO, p1)
				elif event.key == pygame.K_b:
					p2 = list(pygame.mouse.get_pos())

				elif event.key == pygame.K_c:
					l1 = longitud(p1, p2)
					l2 = longitud(p1, CENTRO)
					l3 = longitud(p2, CENTRO)
					perimetro = l1+l2+l3
					print perimetro
					#p2 = trascartesiano(CENTRO, p2)
			pantalla.fill(NEGRO)
			pygame.draw.line(pantalla, VERDE, (CENTRO[0], 0), (CENTRO[0], alto), 4)
			pygame.draw.line(pantalla, VERDE, (0, CENTRO[1]), (ancho, CENTRO[1]), 4)
			pygame.draw.line(pantalla, ROJO, CENTRO, p1, 4)
			pygame.draw.line(pantalla, ROJO, CENTRO, p2, 4)
			pygame.draw.line(pantalla, ROJO, p1, p2, 4)

			pygame.draw.line(pantalla, ROJO, p1, p2, 2)
			pygame.display.flip()



		

		
			

				
		
		pygame.display.flip()
		reloj.tick(10)

	pygame.quit()
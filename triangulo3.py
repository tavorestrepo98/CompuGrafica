import pygame
from funciones import *
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
	pygame.draw.polygon(pantalla, VERDE, [[100, 300], [100, 54], [300, 54]], 5)
	p1 = [100, 300]
	p2 = [100, 54]
	p3 = [300, 54]
	pygame.display.flip()
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			elif event.type == pygame.KEYDOWN:

				xp = input("cuanto quiere escalarlo en x? ")
				yp = input("cuanto quiere escalarlo en y? ")
				lt = [xp, yp]
				p1 = escalamiento(p1, lt)
				p2 = escalamiento(p2, lt)
				p3 = escalamiento(p3, lt)
				pantalla.fill(NEGRO)
				pygame.draw.polygon(pantalla, VERDE, [p1, p2, p3], 5)
				print "Pulso una tecla"
				pygame.display.flip()
	pygame.quit()
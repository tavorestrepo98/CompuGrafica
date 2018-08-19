import pygame

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
	pygame.draw.line(pantalla, BLANCO, (0,0), (100, 199), 2)
	#pygame.draw.polygon(pantalla, VERDE, ((756, 487), (1187, 576), (667, 500)), 8)
	#pygame.draw.polygon(pantalla, BLANCO, ((100, 100), (200, 500), (500, 500), (600, 100)), 30)
	pygame.draw.polygon(pantalla, BLANCO, ((400, 300), (500, 700), (800, 700), (900, 300), (663, 100)), 4)

	pygame.display.flip()
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				print "Boton mouse"
				if event.type == pygame.K_LEFT:
					print "Izquierda"
				#pygame.draw.polygon(pantalla, VERDE, ((100, 100), (200, 500), (500, 500), (600, 100)))
				pygame.display.flip()
	
				
	

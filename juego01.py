import pygame
from funciones import *
from math import *
from dibujos import *
from random import *

ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = 1
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho) or (self.rect.x <= 0):
            self.vel_x = (-1.12)*self.vel_x
        if ((self.rect.y + self.rect.height) >= alto) or (self.rect.y <= 0):
            self.vel_y = (-1.12)*self.vel_y
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.vel_x = 0

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho) or (self.rect.x <= 0):
            self.vel_x = -self.vel_x

        self.rect.x += self.vel_x




if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("juego1")
    jugadores = pygame.sprite.Group()
    j1 = Jugador()
    #j2 = Jugador()
    #j2.rect.x = randrange(ancho-20)
    #j2.rect.y = randrange(alto-20)
    jugadores.add(j1)
    rivales = pygame.sprite.Group()

    for i in range(10):
        r = Rival()
        r.rect.x = randrange(ancho)
        r.rect.y = randrange(alto)
        r.vel_x = randrange(1, 6)
        rivales.add(r)

    pygame.display.flip()
    reloj = pygame.time.Clock()
    fin = False
    puntos = 0

    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.vel_x = 2
                    j1.vel_y = 0
                    #j2.vel_x = 2
                    #j2.vel_y = 0
                elif event.key == pygame.K_LEFT:
                    j1.vel_x = -2
                    j1.vel_y = 0
                    #j2.vel_x = -2
                    #j2.vel_y = 0
                elif event.key == pygame.K_UP:
                    j1.vel_x = 0
                    j1.vel_y = -2
                    #j2.vel_x = 0
                    #j2.vel_y = -2
                elif event.key == pygame.K_DOWN:
                    j1.vel_x = 0
                    j1.vel_y = 2
                    #j2.vel_x = 0
                    #j2.vel_y = 2

        #Control
        ls_colision = pygame.sprite.spritecollide(j1, rivales, True)
        for e in ls_colision:
            puntos += 1
            print puntos



        jugadores.update()
        rivales.update()

        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pygame.display.flip()
        reloj.tick(100)

pygame.quit()

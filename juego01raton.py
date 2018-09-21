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
        self.an = 10
        self.image = pygame.Surface([self.an, self.an])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = 1
        self.vel_x = 0
        self.vel_y = 0

    def update(self, list):
        if ((self.rect.x + self.rect.width) >= ancho) or (self.rect.x <= 0):
            self.vel_x = (-1.12)*self.vel_x
        if ((self.rect.y + self.rect.height) >= alto) or (self.rect.y <= 0):
            self.vel_y = (-1.12)*self.vel_y
        self.image = pygame.Surface([self.an, self.an])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = list[0]
        self.rect.y = list[1]

class Rival1(pygame.sprite.Sprite):
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

class Rival2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(AZUL)
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
    rivales2 = pygame.sprite.Group()

    for i in range(30):
        r = Rival1()
        r.rect.x = randrange(ancho-r.rect.width)
        r.rect.y = randrange(alto-r.rect.height)
        r.vel_x = randrange(1, 6)
        rivales.add(r)

    for i in range(21):
        r = Rival2()
        r.rect.x = randrange(ancho-r.rect.width)
        r.rect.y = randrange(alto-r.rect.height)
        r.vel_x = randrange(1, 6)
        rivales2.add(r)

    pygame.display.flip()
    reloj = pygame.time.Clock()
    fin = False
    puntos = 0

    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        #Control
        ls_colision = pygame.sprite.spritecollide(j1, rivales, True)
        for e in ls_colision:
            j1.an +=5
            jugadores.update(list(pygame.mouse.get_pos()))
            puntos += 1


        ls2_colision = pygame.sprite.spritecollide(j1, rivales2, True)
        for e in ls2_colision:
            j1.an -=5
            jugadores.update(list(pygame.mouse.get_pos()))
            puntos -= 1




        jugadores.update(list(pygame.mouse.get_pos()))
        rivales.update()
        rivales2.update()

        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        rivales2.draw(pantalla)
        pygame.display.flip()
        reloj.tick(100)

    print puntos
    pygame.quit()

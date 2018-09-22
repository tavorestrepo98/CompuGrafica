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

class Muro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 70])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = ancho/2
        self.rect.y = alto/2

    def update(self):
        pass

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.image.fill(AZUL)
        self.muros = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = randrange(1, ancho - self.rect.width)
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho):
            self.rect.x = ancho - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if (self.rect.y + self.rect.height) >= alto:
            self.rect.y = alto - self.rect.height
        if self.rect.x < 0:
            self.rect.x = 1
        self.rect.x += self.vel_x
        ls_col = pygame.sprite.spritecollide(self, self.muros, False)
        for m in ls_col:
            if self.vel_x>0:
                self.rect.right = m.rect.left
            if self.vel_x<0:
                self.rect.left = m.rect.right
        self.rect.y += self.vel_y
        ls2_col = pygame.sprite.spritecollide(self, self.muros, False)
        for k in ls2_col:
            if self.vel_y>0:
                self.rect.bottom = k.rect.top
            if self.vel_y<0:
                self.rect.top = k.rect.bottom


class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.temp = randrange(900, 1400)

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho) or (self.rect.x <= 0):
            self.vel_x = -self.vel_x
        self.rect.x += self.vel_x

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 15])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.vel_y = 7

    def update(self):
        self.rect.y -= self.vel_y

class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.an = 200
        self.image = pygame.Surface([self.an, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.Surface([self.an, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = alto - 40




if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Navesitas")
    jugadores = pygame.sprite.Group()
    vidas = pygame.sprite.Group()


    m1 = Muro()

    v = Vida()
    v.rect.x = 15
    v.rect.y = alto - 40
    vidas.add(v)
    j1 = Jugador()
    j1.rect.y = alto - j1.rect.height-80

    jugadores.add(j1)
    j1.muros.add(m1)


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
                    j1.vel_x = 5
                    j1.vel_y = 0
                elif event.key == pygame.K_LEFT:
                    j1.vel_x = -5
                    j1.vel_y = 0
                elif event.key == pygame.K_UP:
                    j1.vel_x = 0
                    j1.vel_y = -5
                elif event.key == pygame.K_DOWN:
                    j1.vel_x = 0
                    j1.vel_y = 5
            elif event.type == pygame.KEYUP:
                j1.vel_x = 0
                j1.vel_y = 0







        #Control

        jugadores.update()
        vidas.update()

        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        vidas.draw(pantalla)
        j1.muros.draw(pantalla)


        pygame.display.flip()
        reloj.tick(200)



pygame.quit()

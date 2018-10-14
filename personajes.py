import pygame
from funciones import *
from math import *
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
    def __init__(self, an, alt):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, alt])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()

    def update(self):
        pass

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([42, 42])
        self.image.fill(AZUL)
        self.muros = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = randrange(1, ancho - self.rect.width)
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = 0
        self.salud = 20

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho):
            self.rect.x = ancho - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if (self.rect.y + self.rect.height) >= alto-42:
            self.rect.y = alto - self.rect.height - 42
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
        self.image = pygame.Surface([28, 28])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.vel_x = 0
        self.vel_y = 0
        self.temp = 120

    def update(self, muros):
        if self.rect.x < 0:
            self.vel_x = self.vel_x * (-1)

        if ((self.rect.y + self.rect.height) >= alto-42) or (self.rect.y < 0):
            self.vel_y = (-1)*self.vel_y

        ls = pygame.sprite.spritecollide(self, muros, False)
        for i in ls:
            self.vel_x = self.vel_x*(-1)
            self.vel_y = self.vel_y*(-1)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 8])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.vel_y = 0
        self.vel_x = 0

    def update(self):
        self.rect.y -= self.vel_y
        self.rect.x -= self.vel_x
        #self.image = pygame.Surface([10, 10])
        #self.image.fill([180, 12, 130])

class Vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.an = 200
        self.image = pygame.Surface([self.an, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

    def update(self, salud):
        self.an -= salud
        self.image = pygame.Surface([self.an, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = alto - 28

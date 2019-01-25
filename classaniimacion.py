import pygame
from funciones import *
from math import *
from random import *
from personajes import*

class Jugador(pygame.sprite.Sprite):
    def __init__(self, m, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 1
        self.lim = [3, 3, 2, 4, 1, 3, 4, 4, 6, 0]
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pygame.sprite.Group()

    def update(self):
        self.image = self.m[self.accion][self.con]
        if self.accion == 2:
            for e in self.objs:
                pi = [self.rect.x + self.rect.width, self.rect.y]
                if e.rect.collidepoint(pi):
                    print 'golpe'
        if self.con < self.lim[self.accion]:
            self.con +=1
        else:
            self.con = 0
            self.accion = 1
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Objeto(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([70, 80])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.y -= self.vel_y

def recortar(imagen, alto, ancho):
    l1 = []
    l2 = []
    for i in range(0, alto):
        for j in range(0, ancho):
            cuadro = imagen.subsurface(j*70, 80*i, 70, 80)
            l2.append(cuadro)
        l1.append(l2)
        l2 = []
    return l1


ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("KEN")
    img_ken = pygame.image.load('ken.png')
    m = recortar(img_ken, 10, 7)
    j = Jugador(m, [0, 23])
    jugadores = pygame.sprite.Group()
    objetos = pygame.sprite.Group()
    todos = pygame.sprite.Group()

    jugadores.add(j)

    ob = Objeto([150, 200])
    objetos.add(ob)

    todos.add(j)
    todos.add(ob)
    j.objs = objetos
    reloj = pygame.time.Clock()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.vel_x = 6
                    j.vel_y = 0
                if event.key == pygame.K_LEFT:
                    j.vel_x = -6
                    j.vel_y = 0
                if event.key == pygame.K_UP:
                    j.vel_x = 0
                    j.vel_y = -6
                if event.key == pygame.K_DOWN:
                    j.vel_x = 0
                    j.vel_y = 6
                if event.key == pygame.K_z:
                    j.accion = 7
                    j.con = 0
                if event.key == pygame.K_x:
                    j.accion = 2
                    j.con = 0
                if event.key == pygame.K_a:
                    j.accion = 6
                    j.con = 0
                if event.key == pygame.K_s:
                    j.accion = 3
                    j.con = 0
                if event.key == pygame.K_d:
                    j.accion = 8
                    j.con = 0
            if event.type == pygame.KEYUP:
                j.vel_x = 0
                j.vel_y = 0



        todos.update()
        pantalla.fill(NEGRO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(11)

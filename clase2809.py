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
        self.radius = 32

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
        self.temp = randrange(100, 500)

    def update(self, muros):
        if self.rect.x < 0:
            self.vel_x = self.vel_x * (-1)

        if ((self.rect.y + self.rect.height) >= alto-42) or (self.rect.y < 0):
            self.vel_y = (-1)*self.vel_y

        ls = pygame.sprite.spritecollide(self, muros, False)
        for i in ls:
            self.vel_x = self.vel_x*(-1)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.vel_y = 0
        self.vel_x = 0

    def update(self):
        self.rect.y -= self.vel_y
        self.rect.x = self.vel_x

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
        self.rect.y = alto - 28


if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Navesitas")
    jugadores = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    balas1 = pygame.sprite.Group()
    balas2 = pygame.sprite.Group()

    m1 = Muro(87, 230)
    m1.rect.x = 400
    m1.rect.y = 0

    m2 = Muro(80, 305)
    m2.rect.x = 89
    m2.rect.y = 187

    m3 = Muro(60, 69)
    m3.rect.x = 740
    m3.rect.y = 0

    m4 = Muro(70, 370)
    m4.rect.x = 740
    m4.rect.y = 172

    m5 = Muro(177, 79)
    m5.rect.x = 168
    m5.rect.y = 299

    m6 = Muro(220, 73)
    m6.rect.x = 954
    m6.rect.y = 277

    v = Vida()

    vidas.add(v)

    rival1 = Rival()
    rival1.rect.x = 5
    rival1.rect.y = 518
    rival1.vel_x = 2

    rival2 = Rival()
    rival2.rect.x = 578
    rival2.rect.y = 3
    rival2.vel_y = 2


    j1 = Jugador()
    j1.rect.y = randrange(1, 150)
    j1.rect.x = randrange(1, 150)

    jugadores.add(j1)
    j1.muros.add(m1, m2, m3, m4, m5, m6)
    rivales.add(rival1, rival2)
    grito = pygame.mixer.Sound("Wilhelm_Scream.ogg")



    pygame.display.flip()
    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.vel_x = 3.5
                    j1.vel_y = 0
                elif event.key == pygame.K_LEFT:
                    j1.vel_x = -3.5
                    j1.vel_y = 0
                elif event.key == pygame.K_UP:
                    j1.vel_x = 0
                    j1.vel_y = -3.5
                elif event.key == pygame.K_DOWN:
                    j1.vel_x = 0
                    j1.vel_y = 3.5
            elif event.type == pygame.KEYUP:
                j1.vel_x = 0
                j1.vel_y = 0


        for b in j1.muros:
            if pygame.sprite.collide_circle(j1, b):
                grito.play()
                print "Cerca"

        #Control
        jugadores.update()
        vidas.update()
        rivales.update(j1.muros)
        balas1.update()



        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        vidas.draw(pantalla)
        j1.muros.draw(pantalla)
        rivales.draw(pantalla)
        balas1.draw(pantalla)


        pygame.display.flip()
        reloj.tick(200)
        if (j1.rect.x >= ancho-90) and (j1.rect.y <= 90):
            print "GANASTE"
            fin = True





pygame.quit()

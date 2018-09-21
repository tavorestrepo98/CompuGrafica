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
        self.rect.x = randrange(1, ancho - self.rect.width)
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        if ((self.rect.x + self.rect.width) >= ancho):
            self.rect.x = ancho - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 1

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
    v = Vida()
    v.rect.x = 15
    v.rect.y = alto - 40
    vidas.add(v)
    j1 = Jugador()
    j1.rect.y = alto - j1.rect.height-80
    balas = pygame.sprite.Group()
    balas2 = pygame.sprite.Group()
    jugadores.add(j1)
    rivales = pygame.sprite.Group()
    rivals = 20

    for i in range(rivals):
        r = Rival()
        r.rect.x = randrange(ancho-r.rect.width)
        r.rect.y = randrange(alto-j1.rect.height-390)
        r.vel_x = randrange(1, 5)
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
                    for i in range(1, 10):
                        j1.rect.x = j1.rect.x + i
                        jugadores.update()
                        jugadores.draw(pantalla)

                elif event.key == pygame.K_LEFT:
                    for i in range(1, 10):
                        j1.rect.x = j1.rect.x - i
                        jugadores.update()
                        jugadores.draw(pantalla)

                elif event.key == pygame.K_SPACE:
                    b = Bala()
                    b.rect.x = j1.rect.x + (j1.rect.width/2)-8
                    b.rect.y = j1.rect.y
                    balas.add(b)

        #Control



        for r in rivales:
            r.temp -= 1
            if r.temp == 0:
                p = Bala()
                p.rect.x = r.rect.x + 7
                p.rect.y = r.rect.y + r.rect.height
                p.vel_y = 2 * (-1)
                p.image.fill([180, 12, 130])
                balas2.add(p)
                r.temp = randrange(200, 1000)


        for p in balas2:
            p_col = pygame.sprite.spritecollide(p, jugadores, False)
            for e in p_col:
                balas2.remove(p)
                v.an = v.an - 40
            if p.rect.y > alto-80:
                balas2.remove(p)


        for b in balas:
            b_col = pygame.sprite.spritecollide(b, rivales, True)
            for e in b_col:
                balas.remove(b)
                rivals -= 1
            if b.rect.y < -10:
                balas.remove(b)


        jugadores.update()
        rivales.update()
        balas.update()
        balas2.update()
        vidas.update()

        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balas2.draw(pantalla)
        vidas.draw(pantalla)

        pygame.display.flip()
        reloj.tick(200)

        if v.an == 0:
            print "PERDISTE"
            fin = True

        if rivals == 0:
            print "GANASTE"
            fin= True


pygame.quit()

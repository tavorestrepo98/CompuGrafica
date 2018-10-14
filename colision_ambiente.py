import pygame
from funciones import *
from math import *
from random import *
from personajes import*

ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)



if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("LABERINTO")
    jugadores = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    balas = pygame.sprite.Group()



    m1 = Muro(62, 220)
    m1.rect.x = 400
    m1.rect.y = 0

    m2 = Muro(120, 45)
    m2.rect.x = 0
    m2.rect.y = 230

    m3 = Muro(60, 69)
    m3.rect.x = 740
    m3.rect.y = 0

    m4 = Muro(70, 370)
    m4.rect.x = 740
    m4.rect.y = 172

    m5 = Muro(66, 66)
    m5.rect.x = 398
    m5.rect.y = 500

    m6 = Muro(220, 73)
    m6.rect.x = 954
    m6.rect.y = 277

    v = Vida()

    vidas.add(v)

    rival1 = Rival()
    rival1.rect.x = 5
    rival1.rect.y = 518
    rival1.vel_x = 1

    rival2 = Rival()
    rival2.rect.x = 578
    rival2.rect.y = 3
    rival2.vel_y = 1


    j1 = Jugador()
    j1.rect.y = randrange(1, 170)
    j1.rect.x = randrange(1, 170)

    jugadores.add(j1)
    j1.muros.add(m1, m2, m3, m4, m5, m6)
    rivales.add(rival1)
    rivales2.add(rival2)



    pygame.display.flip()
    reloj = pygame.time.Clock()
    fin = False
    mifuente = pygame.font.SysFont("Arial", 60)
    texto = mifuente.render("JUEGO NUEVO", True, ROJO)
    pantalla.blit(texto, [(ancho/2)-189, (alto/2)-30])
    fin2 = False
    pygame.display.flip()
    while not fin2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                fin2 = True

    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.vel_x = 4
                    j1.vel_y = 0
                elif event.key == pygame.K_LEFT:
                    j1.vel_x = -4
                    j1.vel_y = 0
                elif event.key == pygame.K_UP:
                    j1.vel_x = 0
                    j1.vel_y = -4
                elif event.key == pygame.K_DOWN:
                    j1.vel_x = 0
                    j1.vel_y = 4
            elif event.type == pygame.KEYUP:
                j1.vel_x = 0
                j1.vel_y = 0

        #Control
        for r in rivales:
            r.temp -= 1
            if r.temp  == 0:
                p = Bala()
                p.rect.x = r.rect.x + 4
                p.rect.y = r.rect.y
                p.vel_y = 3
                p.image.fill([180, 12, 130])
                balas.add(p)
                r.temp = 120

        for r2 in rivales2:
            r2.temp -= 1
            if r2.temp == 0:
                bal = Bala()
                bal.rect.x = r2.rect.x
                bal.rect.y = r2.rect.y + 5
                bal.vel_x = 2
                bal.image.fill(ROJO)
                balas.add(bal)
                r2.temp = 120

        for p in balas:
            p_col = pygame.sprite.spritecollide(p, jugadores, False)
            p_col2 = pygame.sprite.spritecollide(p, j1.muros, False)
            for e2 in p_col2:
                balas.remove(p)
            for e in p_col:
                balas.remove(p)
            if p.rect.y < 0:
                balas.remove(p)

        




        jugadores.update()
        vidas.update()
        rivales.update(j1.muros)
        rivales2.update(j1.muros)
        balas.update()



        #Refresco de pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        vidas.draw(pantalla)
        j1.muros.draw(pantalla)
        rivales.draw(pantalla)
        rivales2.draw(pantalla)
        balas.draw(pantalla)


        pygame.display.flip()
        reloj.tick(600)

        if (j1.rect.x >= ancho-107) and (j1.rect.y <= 107):
            print "GANASTE"
            fin = True


pygame.quit()

import pygame
import math
import random
ancho=1000
alto=500
centro=[500,250]

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill([250,250,250])
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.radius=10

    def update(self):
        self.rect.x+=self.vel_x
        if(self.rect.x>960):
            self.vel_x=(-1)*self.vel_x
            self.rect.x+=self.vel_x
        elif(self.rect.x<0):
            self.vel_x=(-1)*self.vel_x
            self.rect.x+=self.vel_x

        self.rect.y+=self.vel_y
        if(self.rect.y>420):
            self.vel_y=(-1)*self.vel_y
            self.rect.y+=self.vel_y
        elif(self.rect.y<0):
            self.vel_y=(-1)*self.vel_y
            self.rect.y+=self.vel_y

class rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill([250,0,0])
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.tmp=random.randrange(200,300)

    def update(self):
        self.rect.x+=self.vel_x
        if(self.rect.x>980):
            self.vel_x=(-1)*self.vel_x
            self.rect.x+=self.vel_x
        elif(self.rect.x<0):
            self.vel_x=(-1)*self.vel_x
            self.rect.x+=self.vel_x
        self.tmp-=1

        self.rect.y+=self.vel_y
        if(self.rect.y>460):
            self.vel_y=(-1)*self.vel_y
            self.rect.y+=self.vel_y
        elif(self.rect.y<0):
            self.vel_y=(-1)*self.vel_y
            self.rect.y+=self.vel_y
        #self.tmp-=1

class bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,15])
        self.image.fill([0,255,0])
        self.rect=self.image.get_rect()
        self.vel_y=7
        self.vel_x=7

    def update(self):
        self.rect.y-=self.vel_y
        self.rect.x+=self.vel_x


class Muro(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill([250,250,0])
        self.rect=self.image.get_rect()



if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    salud=120
    grito=pygame.mixer.Sound("grito.ogg")
    jugadores=pygame.sprite.Group()
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    ''''''
    m1 = Muro(200,75)
    m2 = Muro(100,30)
    m3 = Muro(100,300)
    m4 = Muro(100,100)
    m5 = Muro(150,100)
    m6 = Muro(100,150)

    m1.rect.x=750
    m1.rect.y=250
    m2.rect.x=520
    m2.rect.y=0
    m3.rect.x=520
    m3.rect.y=100
    m4.rect.x=300
    m4.rect.y=350
    m5.rect.x=0
    m5.rect.y=100
    m6.rect.x=300
    m6.rect.y=0

    todos.add(m1)
    muros.add(m1)
    todos.add(m2)
    muros.add(m2)
    todos.add(m3)
    muros.add(m3)
    todos.add(m4)
    muros.add(m4)
    todos.add(m5)
    muros.add(m5)
    todos.add(m6)
    muros.add(m6)

    j1=jugador()
    jugadores.add(j1)
    j1.rect.y=0
    j1.rect.x=0

    j2=jugador()
    jugadores.add(j2)
    j2.rect.y=50
    j2.rect.x=900

    balasr=pygame.sprite.Group()
    balas=pygame.sprite.Group()


    rivales=pygame.sprite.Group()

    r1=rival()
    r1.rect.x=0
    r1.rect.y=400
    r1.vel_x=4
    rivales.add(r1)

    r2=rival()
    r2.rect.x=480
    r2.rect.y=250
    r2.vel_y=4
    rivales.add(r2)

    r3=rival()
    r3.rect.x=600
    r3.rect.y=350
    r3.vel_x=4
    rivales.add(r3)

    #ciclo del juego
    reloj=pygame.time.Clock()
    fin=False
    salud=120
    tem=10
    enemigos=0
    bal=0
    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    j1.vel_y=-2
                    j1.vel_x=0
                if event.key == pygame.K_DOWN:
                    j1.vel_y=2
                    j1.vel_x=0
                if event.key == pygame.K_LEFT:
                    j1.vel_x=-2
                    j1.vel_y=0
                if event.key == pygame.K_RIGHT:
                    j1.vel_x=2
                    j1.vel_y=0
                if event.key == pygame.K_SPACE:
                    b=bala()
                    b.vel_x=7
                    b.vel_y=0
                    b.rect.x=j1.rect.x+17
                    b.rect.y=j1.rect.y
                    balas.add(b)
                    bal+=1






        #logica del juego


        for b in muros:
            if pygame.sprite.collide_circle(j1,b):
                grito.play()


        ls_col = pygame.sprite.spritecollide(j1, muros, False)
        for m in ls_col:
            if (j1.vel_x > 0) and (j1.rect.right >= m.rect.left):
                j1.vel_x = 0
                j1.rect.right = m.rect.left
            if (j1.vel_y > 0) and (j1.rect.bottom >= m.rect.top):
                j1.vel_y = 0
                j1.rect.bottom = m.rect.top
            if (j1.vel_x < 0) and (j1.rect.left <= m.rect.right):
                j1.vel_x = 0
                j1.rect.left = m.rect.right
            if (j1.vel_y < 0) and (j1.rect.top <= m.rect.bottom):
                j1.vel_y = 0
                j1.rect.top = m.rect.bottom

        ls_colr = pygame.sprite.spritecollide(r1, muros, False)
        for m in ls_colr:
            if (r1.vel_x > 0) and (r1.rect.right >= m.rect.left):
                r1.vel_x-=5
            if (r1.vel_x < 0) and (r1.rect.left <= m.rect.right):
                r1.vel_x = -4

        ls_colr2 = pygame.sprite.spritecollide(r3, muros, False)
        for m in ls_colr2:
            if (r3.vel_x > 0) and (r3.rect.right >= m.rect.left):
                r3.vel_x = -4
            if (r3.vel_x < 0) and (r3.rect.left <= m.rect.right):
                r3.vel_x = 4



        if r1.tmp < 0:
            br1=bala()
            if((r1.rect.right<550) and (r1.rect.left>200)):
                br1.vel_y=7
                br1.vel_x=0
                br1.rect.x=r1.rect.x
                br1.rect.y=r1.rect.y
                balasr.add(br1)
                r1.tmp=random.randrange(10,20)

        if r2.tmp < 0:
            br2=bala()
            if((r2.rect.bottom<350) and (r2.rect.top>200)):
                br2.vel_x=-7
                br2.vel_y=0
                br2.rect.x=r2.rect.x
                br2.rect.y=r2.rect.y
                balasr.add(br2)
                r2.tmp=random.randrange(5,15)

        if r3.tmp < 0:
            br3=bala()
            if((r3.rect.right<750) and (r3.rect.left>600)):
                br3.vel_y=7
                br3.vel_x=0
                br3.rect.x=r3.rect.x
                br3.rect.y=r3.rect.y
                balasr.add(br3)
                r3.tmp=random.randrange(10,20)

        for blr in balasr:
            br_col=pygame.sprite.spritecollide(blr,jugadores,False)
            for e in br_col:
                salud-=12
                print salud
                balasr.remove(blr)
            if blr.rect.y>440:
                balasr.remove(blr)
            if blr.rect.x<0:
                balasr.remove(blr)
            if blr.rect.y<0:
                balasr.remove(blr)



        jugadores.update()
        rivales.update()
        balasr.update()
        balas.update()

        #resfresco de pantalla
        pantalla.fill([0,0,0])
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balasr.draw(pantalla)
        balas.draw(pantalla)
        todos.draw(pantalla)
        pygame.draw.line(pantalla,0xff2d00,[0,500],[salud,500],50)
        pygame.display.flip()
        reloj.tick(60)

#rosa de n petalos
import pygame
import math


ancho=600
alto=600
centro=[300,300]

def apantalla(c,p):
    x = c[0] + p[0]
    y = c[1] - p[1]
    return [x,y]

def acartesiana(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

def pcartesiana(r,S):
    x=int(r*math.cos(math.radians(S)))
    y=int(r*math.sin(math.radians(S)))
    return [x,y]

if __name__ == '__main__' :
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.draw.line(pantalla,0xff2d00,[0,300],[600,300])
    pygame.draw.line(pantalla,0xff2d00,[300,0],[300,600])
    x=0
    y=0
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


        x+=0.108
        y+=0.7
        #r=int(280*math.cos(math.radians(5*x)))#flor n petalos
        #r = 200#circunferencia
        #r = 1 + 0.1*x#espiral de arquimedes
        #r = int(60/(1 + 0.8*math.cos(math.radians(x))))#elipse
        #r = int(60/(1 + 1.8*math.cos(math.radians(x-10))))  #hiperbola
        r = 100 + 100*math.cos(math.radians(x))#cardioide
        #r = 50 + 80*math.cos(math.radians(x))#caracol con lazo interno

        #print x
        #pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,0xff2d00,apantalla(centro,(pcartesiana(r,x))),2)
        #pygame.draw.line(pantalla,[0,250,0],centro,apantalla(centro,(pcartesiana(r,x))))

        pygame.display.flip()
        reloj.tick(550)

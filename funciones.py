from math import *
from random import *
import pygame

ancho = 1300
alto = 710
CENTRO = (ancho/2, alto/2)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

def traslacion(l, l2):
	x = l[0]+l2[0]
	y = l[1]+l2[1]
	return [x, y]

def trascartesiano(l, l2):
	x = l[0]+l2[0]
	y = l[1]-l2[1]
	return [x, y]

def rotacion(p, angulo):
	x = p[0]*cos(angulo) - p[1]*sin(angulo)
	y = p[0]*sin(angulo) + p[1]*cos(angulo)
	return [x,y]

def rotacionhoraria(p, angulo):
	x = p[0]*cos(angulo) + p[1]*sin(angulo)
	y = -p[0]*sin(angulo) + p[1]*cos(angulo)
	return [x,y]

def escalamiento(punto, e):
	x = punto[0]*e[0]
	y = punto[1]*e[1]
	return [x,y]

def longitud(l1, l2):
	return sqrt(((l1[0]-l2[0])*(l1[0]-l2[0])) + ((l1[1]-l2[1])*(l1[1]-l2[1])))

def pant_cart2(centro, punto):
	x = punto[0] - centro[0]
	y = centro[1]-punto[1]
	return [x,y]

def rot_punto(fijo, punto):
	x = punto[0]-fijo[0]
	y = punto[1]-fijo[1]
	return [x, y]

def polares(r, angulo):
	x = int(r*cos(radians(angulo)))
	y = int(r*sin(radians(angulo)))
	return [x, y]


def tras_centro(p1, p2):
	x = p2[0]-p1[0]
	y = p2[1]-p1[1]
	return [x, y]

def tras_original(p1, p2):
	x = p2[0]+p1[0]
	y = p2[1]+p1[1]
	return [x, y]


def movimientoabajo(imagen, pantalla):
	i = 0
	j = 2000
	while j>0:
		pantalla.fill(NEGRO)
		pantalla.blit(imagen[0][i], [0,0])
		pygame.display.flip()
		if i<2:
			i+=1
		else:
			i = 0
		j-=1

import pygame
from funciones import *
from math import *

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
pygame.init()

def circulo(pantalla, centro, radio):
    pygame.draw.circle(pantalla, VERDE, centro, radio)

def rectangulo(pantalla, p):
    pygame.draw.rect(pantalla, VERDE, p, 3)

def punto(pantalla, centro):
    pygame.draw.circle(pantalla, VERDE, centro, 2)

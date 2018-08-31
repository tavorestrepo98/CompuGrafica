from math import *
from random import *
#taller parte1

def sumamatrices(list1, list2, n):
	resultado = []
	momentaneo = []
	for i in xrange(0,n):
		momentaneo= []
		for j in range(0,n):
			momentaneo.append(list1[i][j] + list2[i][j])
		resultado.append(momentaneo)
	return resultado


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

def pant_cart(l1, l2):
	x = l2[0]-l1[0]
	y = l1[1]-l2[1]
	return [x, y]

'''
def matrizidentidad(n):
	resultado = []
	temp = []
	index = 0
	for i in range(0,n):
		temp = []
		for j in range(n):
			temp.append(0)
		temp[index] = 1
		resultado.append(temp)
		index = index + 1
	return resultado

def columna(l, m):
	column = []
	for i in range(len(l)):
		column.append(l[i][m])
	return column

#taller parte2

def random():
	lis = []
	for i in range(5):
		lis.append(randrange(50))
	return lis

def hipotenusa():
	catetoa = input("Digite el valor del primer cateto: ")
	catetob = input("Digite el valor del segundo cateto: ")
	print "Los angulos del triangulo son: " + str(pi/2) + ", " + str((pi/2)-atan(catetoa/catetob)) + ", " + str(atan(catetoa/catetob))
	return "El valor de la hipotenusa es: " + str(sqrt((catetoa * catetoa) + (catetob * catetob)))
'''

'''
for x in range(0,11):
	print(x)

print("===========================")

for x in range(4,11):
	print(x)

print("==========================")


a = int(input("Ingrese un  valor: "))
for x in range(2,a,2):
	print(x)

print("===========================")

for x in range(3, 21, 3):
	print(x)


print "1.==============================="
lista1=[]
print lista1
a = input("Ingrese un elemento: ")
lista1.append(a)
print lista1

print "\n2.================================"
lista2 = []
i = 0
while i < 5:
	lista2.append(input())
	i = i+1
print lista2


print "\n3.==============================="
lista3=[]
elemnto3 = input("Cuantos elementos quiere ingresar? ")
a=0
while a < elemnto3:
	lista3.append(input())
	a = a+1
print lista3


print "\n4.==============================="

lista4 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for x in lista4:
	print x[0], x[1], x[2]

print"\n5.================================="

lista5 = [1, 3.4, "e", True, ["hola", False], 4]
print lista5

for element in lista5:
	if type(element) != (type(4) or type(1.3)):
		lista5.remove(element)

print lista5

'''

'''
print "1.===================================="
ls1 = [1, 3, 5.6, 4, True]
ls2 = [[1,2,3], False, "hoola"]
ls3 = ls1 + ls2
print ls1,"\n", ls2, "\n", ls3

print"\n2.====================================="
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [2, 4, 6, 8, 10]

for x in lista1:
	if x in lista2:
		print x

print "\n3.===================================="
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista4 = [2, 4, 6, 8, 10]

for x in lista3:
	if x in lista4:
		pass
	else:
		print x

print "\n4.====================================="
l1 = [1, 0, 3]
l2 = [0, 4, -1]
l3 = []
i = 0
while i < 3:
	l3.append(l1[i] + l2[i])
	i = i+1
print l3
'''
print "\n1.========================================="

seleccion = {"portero":["David Ospina", "Vargas"], "defensa":["Yerri Mina", "Oscar Murillo", "Santiago Arias", "Armero"], "centro": ["J"]}



































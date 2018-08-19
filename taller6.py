from funciones import *
from math import *

if __name__ == '__main__':
    lista1 = [[1,2,3], [4, 5, 6], [7, 8, 9]]
    lista2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#    listaresult = sumamatrices(lista1, lista2, 3)
#    print listaresult

    #print productopunto([1, 0, 3], [3, 2, 1])
    '''
    print random()
    print multiplicacionmatrices([[1,0,1],[0,1,2]], [[3,5],[-1,0],[2,-1]])
    print matrizidentidad(4)
    print columna([[1, 0, 3], [3, 2, 1]], 2)
    print hipotenusa()
    print multiplicacionmatrices([[2,5,4], [1,0,6], [1,1,1]], matrizidentidad(3))
    print columna(matrizidentidad(4), 1)'''

    x = input("Digite la posicion en x del punto: ")
    y = input("Digite la posicion en y del punto: ")
    #angulos = input("cuanto quiere rotarlo: ")
    #print rotacion([x, y], pi/2)
    print escalamiento([x, y], [2, 2])

    #tx = input("Digite el desplazamiento en x del punto: ")
    #ty = input("Digite el desplazamiento en y del punto: ")
    
    #vec1=[[x], [y], [1]]
    #mat1 = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]
    #print traslacion(mat1, vec1)

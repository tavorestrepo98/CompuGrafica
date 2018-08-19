class Mascota:
    def __init__(self, nombre, propietario = "anonimo"):
        self.nombre = nombre
        self.propietario = propietario
    def registro(self):
        return self.nombre + " " + self.propietario


class Matriz:
    def __init__(self, fila, columna, mat):
        self.fila = fila
        self.columna = columna
        self.mat = mat
    def retornarfila(self, n):
        return self.mat[n]
    def retornarcolumna(self, n):
        momentanea = []
        for x in xrange(len(self.mat)):
            momentanea.append(mat[x][n])
        return momentanea
    def dimension(self):
        return str(self.fila)+"X"+str(self.columna)
    def agregarfila(self, fila):
        self.mat.append(fila)
    def matriz(self):
        return mat
    def agregarcolumna(self, columna):
        for i in range(len(mat)):
            self.mat[i].append(columna[i])


if __name__ == '__main__':
    mat = [[1,2], [3,4]]
    fila = len(mat)
    columna = len(mat[0])
    mimatriz = Matriz(fila, columna, mat)
    print mimatriz.dimension()
    print mimatriz.retornarfila(0)
    mimatriz.agregarfila([0, 7])
    print mimatriz.matriz()
    

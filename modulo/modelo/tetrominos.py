class Tetromino:
    def __init__(self, forma):
        self.forma = forma

    def rotacion(self):
        filas = len(self.forma)
        columnas = len(self.forma[0])

        matriz_rotada = [[0 for _ in range(filas)] for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                matriz_rotada[j][filas - i - 1] = self.forma[i][j]

        return Tetromino(matriz_rotada)


    def representacion(self):
        return '\n'.join([''.join(['@' if cell == 1 else '.' for cell in row]) for row in self.forma])


    def igualdad(self, otro):
        return self.forma == otro.forma


    def semejanza(self, otro):
        forma_inicial = self.forma

        for _ in range(4):
            if self.forma == otro.forma:
                return True
            self.rotacion()
        self.forma= forma_inicial
        return False

    def guardar_estado(self, filename, character='@'):
        with open(filename, 'w') as file:
            file.write(self.representacion(character))




I = Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]])

O = Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

T = Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 1],
              [0, 0, 1, 0],
              [0, 0, 0, 0]])

S = Tetromino([[0, 0, 0, 0],
              [0, 0, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

Z = Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [0, 0, 0, 0]])

J = Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

L = Tetromino([[0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])


rotacionI= I.rotacion()
print("Rotación1 de I:")
print(rotacionI.representacion())


rotacionI.rotacion()
print("Rotación de I (180 grados):")
print(I.representacion())


if I.igualdad(J):
    print("Los Tetrominos I y J son iguales.")
else:
    print("Los Tetrominos I y J son diferentes.")


O.rotacion().rotacion()

O_rotada=Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

if O.igualdad(O.rotacion()):
    print(f"Los Tetrominos O y O rotada dos veces son iguales.")
else:
    print(f"Los Tetrominos O y O rotada dos veces son diferentes.")










J.rotacion()
print("J rotada")
print(J.representacion())


L_rotada = L.rotacion()
L_rotada2 = L_rotada.rotacion()
L_rotada3 = L_rotada2.rotacion()
print("L rotada tres veces ")
print(L_rotada3.representacion())

if J.rotacion().semejanza(L):
    print(f"Los Tetrominos J rotada y L rotada 3 veces son semejantes.")

else:
    print(f"Los Tetrominos J rotada  y L rotada 3 veces no son semejantes")







from dataclasses import dataclass


@dataclass
class Tetromino:

    def __init__(self, estado_actual):
        forma_actual: []


    def rotacion(self, una_rotacion, dos_rotaciones, tres_rotaciones):
        una rotacion

    def representacion(self, inicical, una_rotacion, dos_rotaciones):
        pass


    def igualdad(self):
        pass


    def semejanza(self):
        pass


I= Tetromino()
O= Tetromino()
T= Tetromino()
S= Tetromino()
Z= Tetromino()
J= Tetromino()
L= Tetromino()




#i o j s z l son objetos de la clase tetromino
# cada objeto puede rotar 90 a la derecha por lo que puede tener 4 estados, cada objeto esta formado por 4 fragmentos
#la primera columna es el estado inicial, la segunda es una rotacion de 90
# solo debo hacer el componente que representa los tertominos)
# clase tertomino (llamar al metodo rotacion para hacer la rotacion (llamar al metoro representacion (debe tener un constructor
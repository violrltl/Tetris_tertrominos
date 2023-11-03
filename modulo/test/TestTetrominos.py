from modulo.modelo.tetrominos import Tetromino

def test_rotacion():

    I =  Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]])


    rotado = I.rotacion()

    resultado_esperado = Tetromino([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 0, 0]])

    assert rotado.igualdad(resultado_esperado)


def test_igualdad():

    O_rotada= Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

    J = Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

    O = Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

    assert O.igualdad(O_rotada)
    assert not J.igualdad(O)





def test_semejanza():

      I =  Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]])

      J = Tetromino([[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

      O = Tetromino([[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]])

      assert not I.semejanza(J)
      assert not I.semejanza(O)














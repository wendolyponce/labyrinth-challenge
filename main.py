import queue

#paso 1: Representar la estructura del laberinto
#paso 2: Representar/definir estructura de la barra
#paso 3: Implementar funciones auxiliares (movimiento, limitaciones)
#paso 4: Implementar funcion principal
#paso 5: Realizar pruebas
#paso 6: Optimizar ()


# Definimos dos laberintos, labyrinth1 y labyrinth2
labyrinth1 = [['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','.','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'],]

labyrinth2 = [['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'],]

def print_labyrinth(labyrinth, path = ""):
    
    Posición inicial (0, 0)
    i = 0
    j = 0
    pos = set()

    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((i, j))
    
    for j, row in enumerate(labyrinth):
        for i, col in enumerate(row):
                print(col + ".", end="")
        print()


def print_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

print_laberinto(laberinto1)

def coordenada_valida(x, y, laberinto):
    """
    Determinar si el movimiento es posible dentro del laberinto
    Args:
        x: coordenada x
        y: coordenada y
        laberinto: matriz del laberinto
    Returns:
        bool: True si es posible, False en caso contrario
    """
    fila    = len(laberinto)
    columna = len(laberinto[0])

    if 0 <= x < fila and 0 <= y < columna and laberinto[x][y] == '.':
        resultado = True

    return resultado

def movimientos(x, y, orientacion, laberinto):
    """
    posibles_movimientos = [der,izq,arriba,abajo]
    mover der x, y+1 -> 0, 1
    mover izq x, y-1 -> 0,-1

    mover arriba x-1, y -> -1,0
    mover abajo  x+1, y ->  1,0
    """

    posibles_movimientos = [(0,1),(0,-1),(-1,0),(1,0)]
    
    dx, dy = orientacion

    for i, j in posibles_movimientos:
        new_x = x + i
        new_y = y + j

        if (
            coordenada_valida(x, y - 1, laberinto) and
            coordenada_valida(x, y, laberinto) and
            coordenada_valida(x, y + 1, laberinto)
        ):



        #print(i," ", j)

    return 0

movimientos(0, 1, 0, laberinto)









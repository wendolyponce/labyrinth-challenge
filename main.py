#paso 1: Representar la estructura del laberinto
#paso 2: Representar/definir estructura de la barra
#paso 3: Implementar funciones auxiliares (movimiento, limitaciones)
#paso 4: Implementar funcion principal
#paso 5: Realizar pruebas
#paso 6: Optimizar ()

laberinto = [['.','.','.','.','.','.','.','.','.'],
             ['#','.','.','.','#','.','.','.','.'],
             ['.','.','.','.','#','.','.','.','.'],
             ['.','#','.','.','.','.','.','#','.'],
             ['.','#','.','.','.','.','.','#','.'],]




#Posición inicial, barra = (x, y, orientación) donde 0 es horizontal y 1 vertical
posicion_barra = (0, 0, (0)) #La barra inicia con orientación horizontal

#barra_posicion_inicial = (0,1,2)

posicion_inicial = (0, 0)
posicion_final = (fila, columna)

def print_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

print_laberinto(laberinto)


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

    if laberinto[x][y] == '.':
        resultado = True

    return resultado


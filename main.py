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

# Definimos la función print_labyrinth para imprimir el laberinto seguimiento de ruta
def print_labyrinth(labyrinth, path = ""):
    """
    Imprime el laberinto con la ruta recorrida
    
    Args:
        labyrinth (list): El laberinto representado como una lista de listas
        path (str): Cadena que contiene la ruta recorrida ("L", "R", "U" y "D"). Por defecto, es una cadena vacía
    """
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
                print(col + ".", end = "")
        print()

# Definimos la función valid para comprobar si un movimiento es válido dentro del laberinto
def valid(labyrinth, moves):
    """
    Verifica si es un movimiento válido dentro del laberinto

    Args:
        labyrinth (list): El laberinto representado como una lista de listas
        moves (str): Cadena que contiene la ruta recorrida ("L", "R", "U" y "D"). Por defecto, es una cadena vacía
    
    Returns:
        bool: True el movimiento es válido, False en caso contrario
    """
    i = 0
    j = 0

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
    # Verifica si las coordenadas estan dentro de los límites del laberinto
    if not (0 <= i < len (labyrinth[0]) and 0 <= j < len (labyrinth)):
        return False
    # Verifica si la celda es una pared
    elif (labyrinth[j][i] == "#"):
        return False
    
    return True

def solution(labyrinth, moves):
    """
    Verifica si el recorrido llegó a la esquina inferior derecha

    Args:
        labyrinth (list): El laberinto representado como una lista de listas
        path (str): Cadena que contiene la ruta recorrida ("L", "R", "U" y "D"). Por defecto, es una cadena vacía
    
    Returns:
        bool: True si encontro una solución, False en caso contrario
    """
    i = 0
    j = 0

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
    
    a = len(labyrinth[0]) - 1
    b = len(labyrinth) - 1 
    
    #Verifica si llegó a la esquina inferior derecha
    if i == a and j == b:
        #print("Movimientos: " + moves)
        print_labyrinth (labyrinth, moves)
        return True
    
    return False

# MAIN

# Utilizamos una cola para realizar la búsqueda en anchura
nums = queue.Queue()
nums.put("")
add = ""
labyrinth = labyrinth1

# Realizamos la búsqueda hasta encontrar la solución (esquina inferior derecha del laberinto)
while not solution(labyrinth,add):
    add = nums. get()

    for j in ["L","R","U","D"]:
        put = add + j

        if valid(labyrinth, put):
            nums.put(put)

# Imprimimos la longitud de la ruta
print(len(add))









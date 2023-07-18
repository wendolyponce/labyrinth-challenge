#paso 1: Definir universo
#paso 2: Definir el objeto/barra
#paso 3: Definir estado inicial
#paso 4: Definir movimientos


laberinto = [['.','.','.','.','.','.','.','.','.'],
             ['#','.','.','.','#','.','.','.','.'],
             ['.','.','.','.','#','.','.','.','.'],
             ['.','#','.','.','.','.','.','#','.'],
             ['.','#','.','.','.','.','.','#','.'],]
    
fila = len(laberinto)
columna = len(laberinto[0])
print(fila)
print(columna)

#print(laberinto[4][1])

barra_posicion_inicial = (0,1,2)

posicion_inicial = (0, 0)
posicion_final = (fila, columna)

def print_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

print_laberinto(laberinto)



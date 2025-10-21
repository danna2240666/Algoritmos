# Matrices triangulares (ID 160)
# Verifica si una matriz cuadrada es triangular superior o inferior

def es_triangular(matriz, n):
    # Verifica si es triangular superior (todo bajo la diagonal es 0)
    superior = True
    for i in range(1, n):
        for j in range(i):
            if matriz[i][j] != 0:
                superior = False
                break

    # Verifica si es triangular inferior (todo sobre la diagonal es 0)
    inferior = True
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != 0:
                inferior = False
                break

    # Si cumple cualquiera de las dos condiciones, es triangular
    return superior or inferior

# Programa principal
while True:
    n = int(input("Ingrese el tamaño de la matriz (0 para terminar): "))
    if n == 0:
        break

    matriz = []
    print(f"Ingrese los {n}x{n} elementos de la matriz:")
    for i in range(n):
        fila = list(map(int, input(f"Fila {i + 1}: ").split()))
        matriz.append(fila)

    if es_triangular(matriz, n):
        print("SI")
    else:
        print("NO")


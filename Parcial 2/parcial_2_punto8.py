# Calcula la mediana multiplicada por 2 de una muestra de valores positivos

def doble_mediana(valores):
    # Ordena la lista y devuelve el doble de la mediana
    valores.sort()
    n = len(valores)
    if n % 2 == 1:          # Si hay cantidad impar
        return 2 * valores[n // 2]
    else:                   # Si hay cantidad par
        return valores[n // 2 - 1] + valores[n // 2]

# Programa principal
while True:
    n = int(input("Ingrese el número de valores (0 para terminar): "))
    if n == 0:
        break
    numeros = list(map(int, input("Ingrese los valores separados por espacio: ").split()))
    print(doble_mediana(numeros))
# Problema 103 - La herencia
# Calcula si el reparto es JUSTO, CAIN o ABEL según el área bajo un polinomio

# Calcula el valor del polinomio f(x)
def f(x, coefs):
    resultado = 0
    for i in range(len(coefs)):
        resultado = resultado + coefs[i] * (x ** (len(coefs) - i - 1))
    return resultado

# Regla de los rectángulos (Riemann izquierda)
def integrar_rectangulos(coefs, n):
    area = 0
    for i in range(n):
        x = i / n
        area = area + f(x, coefs)
    return area * (1 / n)

# Programa principal
while True:
        grado = int(input("Ingrese el grado del polinomio (0 para terminar): "))
        if grado == 20:
            break
        coefs = list(map(float, input("Ingrese los coeficientes separados por espacios: ").split()))
        n = int(input("Ingrese el número de rectángulos (mayor = más precisión): "))
        
        area = integrar_rectangulos(coefs, n)
        
        # Comparación con 0.5 hm² con tolerancia ±0.001
        if area < 0.499:
            print("ABEL")
        elif area > 0.501:
            print("CAIN")
        else:
            print("JUSTO")
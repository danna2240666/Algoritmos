def encontrar_pares_unicos(lista, objetivo):
    vistos = set()
    pares = set()

    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            pares.add(tuple(sorted((num, complemento))))
        vistos.add(num)

    if pares:
        for a, b in sorted(pares):
            print(f"{a}, {b}")
    else:
        print("No se encontraron pares que sumen", objetivo)


# Programa principal
numeros = input("Ingrese los números separados por comas: ")
lista = [int(x.strip()) for x in numeros.split(",") if x.strip()]
objetivo = int(input("Ingrese la suma objetivo: "))

encontrar_pares_unicos(lista, objetivo)

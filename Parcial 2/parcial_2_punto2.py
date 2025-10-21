# Programa: Cifrado César con saltos alternos (3 y 4)

def cifrar_palabra(palabra, salto):
    """Cifra una sola palabra con el cifrado César."""
    abecedario_min = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""

    for letra in palabra:
        if letra in abecedario_min:
            nueva_pos = (abecedario_min.index(letra) + salto) % len(abecedario_min)
            resultado += abecedario_min[nueva_pos]
        elif letra in abecedario_may:
            nueva_pos = (abecedario_may.index(letra) + salto) % len(abecedario_may)
            resultado += abecedario_may[nueva_pos]
        else:
            resultado += letra  # Mantener signos o caracteres no alfabéticos
    return resultado


def descifrar_palabra(palabra, salto):
    """Descifra una sola palabra con el cifrado César."""
    return cifrar_palabra(palabra, -salto)


def procesar_texto(texto, modo="cifrar"):
    """Cifra o descifra un texto completo alternando los saltos 3 y 4."""
    palabras = texto.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        # Palabras impares usan salto 4, pares salto 3
        salto = 4 if (i + 1) % 2 != 0 else 3

        if modo == "cifrar":
            resultado.append(cifrar_palabra(palabra, salto))
        else:
            resultado.append(descifrar_palabra(palabra, salto))

    return " ".join(resultado)


# --- Programa principal ---
print("=== CIFRADO CÉSAR CON SALTOS ALTERNOS ===")
texto = input("Ingrese el texto: ")
accion = input("¿Desea cifrar o descifrar? (c/d): ").lower()

if accion == "c":
    print("Texto cifrado: ", procesar_texto(texto, "cifrar"))
elif accion == "d":
    print("Texto descifrado: ", procesar_texto(texto, "descifrar"))
else:
    print("Opción no válida. Debe escribir 'c' o 'd'.")

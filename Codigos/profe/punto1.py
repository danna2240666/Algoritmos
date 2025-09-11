opcion = 1
while opcion != 0 :
    print("1. Seno") 
    print("2. Coseno")
    print("3. Tangente")
    print("0. Salir")
    opcion = int(input("> "))
    if opcion == 3 :
        print("La tangente no está implementada.")
    elif opcion == 1:
        suma = 0
        n = int(input("Numero de pasos de calculo: "))
        x = int(input("Angulo en grados: "))
        x = (3.14159 / 180) * x
        # x =  (180 / math.pi) * x
        for i in range(n):
            fact = 1
            temp = 2 * i + 1
            while temp > 1 :
                fact = fact * temp
                temp = temp - 1
            # fact es el valor del denominador
            suma = suma + (( (-1)**i ) * ( x ** (2 * i + 1) )) / fact
        print(suma)
        # hasta aca seno
    elif opcion == 2:
        suma = 0
        n = int(input("Numero de pasos de calculo: "))
        x = int(input("Angulo en grados: "))
        x = (3.14159 / 180) * x
        # x =  (180 / math.pi) * x
        for i in range(n):
            fact = 1
            temp = 2 * i
            while temp > 1 :
                fact = fact * temp
                temp = temp - 1
            # fact es el valor del denominador
            suma = suma + (( (-1)**i ) * ( x ** (2 * i) )) / fact
        print(suma)
    else :
        print("Opcion incorrecta")
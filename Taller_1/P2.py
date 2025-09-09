n= int(input("Ingrese el valor para comprobar si tiene raiz entera: "))

#Se le da un valor inicial a i para referenciarlo mas adelante
i=1

#Mientras n no tenga raiz entera i, se prueba el siguiente numero, por ello i= i+1
while n!=i**2:
    #En caso de haber probado cada numero menor que n y ninguno halla sido su raiz, se concluye que no tiene una
    if i==n:
        print(f"{n} no tiene una raiz entera")
        #Sabiendo que no tiene raiz exacta, se para el programa
        exit()
    i= i+1
#Cuando n sea igual a su raiz entera al cuadrado, se entrega ese valor
else:
    print(f"{n} tiene raiz entera {i}")

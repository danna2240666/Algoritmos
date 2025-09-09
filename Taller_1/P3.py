#Escribir un numero n en base b de otro se hace dividiendo n sobre b y tomando su residuo para escribir su nueva representacion, el resultado de esa division
#se vuelve a dividir entre b y asi sucesivamente, escribiendo los residuos, hasta que la division (entera) de 1 o 0, poniendo este numero de ultimas en la respuesta

#Los datos deben obligarse a ser enteros para no incluir puntos en el resultado
n= int(input("Ingrese el numero a representar en base b: "))
b= int(input("Ingrese la base b: "))

if b>9:
    print("Por favor ingrese un valor entre 1 y 9")

#d sera la division de n entre un multiplo de b para obtener su residuo
d= n
suma= ""
i=1

#Mientras n se pueda dividir entre b, continua la operacion
while d>1:
    #Los residuos se deben volver texto para escribirlos lado a lado
    r= str(d%b)
    suma= r + suma
    #Seguir dividiendo los resultados por b, se puede ver como dividir n sobre b, i veces
    d= int(n/b**i)
    i= i+1
#Si el residuo da 1, se pone este junto a los residuos de las divisiones
if d==1:
    suma= "1" + suma
    print(suma)
#Si es 0, se ignora y se toman los residuos
else:
    print(suma)

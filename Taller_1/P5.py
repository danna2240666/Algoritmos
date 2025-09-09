#Toma el numero como texto
n= input("Ingrese el numero a cambiar: ")

#Se le da un valor inicial del ultimo elemento del numero
suma= n[len(n)-1]

#El loop da pasos hacia atras para evitar que el numero final tenga un 0 a su derecha
for i in range(len(n)-2, -1, -1):
    suma= n[i] + "0" + suma

print(suma)
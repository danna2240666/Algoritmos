import random as rnd

lista = []
suma= 0

#Se genera una lista de 100 elementos al azar con valores entre 0 y 50
for i in range(100):
    lista.append(rnd.randint(0, 50))
print(f"La lista generada es: {lista}")

#Se calcula la sumatoria de todos los elementos y se divide entre 100 (valor total elementos) para calcular la media
for i in range(len(lista)):
    suma= suma + lista[i]
media= suma/100
print(f"La media de esta lista es: {media}")

menores= []
mayores= []

for i in range(len(lista)):
    #Si el valor en la lista es menor a la media, se agrega a la sublista con todos los elementos que cumplan la condicion
    if lista[i]<media:
        menores.append(lista[i])
    #Si es mayor, se agrega a la otra sublista
    elif lista[i]>media:
        mayores.append(lista[i])
#Se muestran ambas listas con el valor total de elementos en cada una que en conjunto debe ser menor o igual a 100
print(f"La sublista con los numeros menores a la media tiene {len(menores)} elementos y es de la forma: {menores}")
print(f"La sublista con los numeros mayores a la media tiene {len(mayores)} elementos y es de la forma: {mayores}")
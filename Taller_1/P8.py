n= int(input("Ingrese el numero de elementos de la lista: "))

lista= []

print(f"Ingrese los {n} valores de la lista: ")
for i in range(n):
    valor= int(input(f"{i+1}. "))
    lista.append(valor)
print(f"Su lista es de la forma {lista}")

#Lista donde se guarda las repeticiones de cada numero
conteos = []

for i in range(len(lista)):
    conteo = 0
    for j in range(len(lista)):
        #Si un numero se repite, agregar +1 a su cantidad total
        if lista[j] == lista[i]:
            conteo = conteo + 1
    conteos.append(conteo)

moda= conteos[0]
num= lista[0]
for i in range(1, len(conteos)):
    #Se compara la cantidad de repeticiones del primer elemento para ver si es mayor al resto, si no lo es, se prueba con el siguiente puesto
    #Solo un valor de repeticion sera mayor al resto
    if conteos[i]>moda:
        moda= conteos[i]
        num= lista[i]

#Lista con los valores que tienen la repeticion de moda
nums= []
for j in range(len(lista)):
    if conteos[j]==moda:
        rep= False
        #Rep= true si la repeticion de un numero es igual a la repeticion de la moda y ya esta en la lista
        for k in range(len(nums)):
            if lista[j]== nums[k]:
                rep= True
        #Si la repeticion del numero es igual a la repeticion de moda y no esta en la lista, se agrega
        if rep== False:
            nums.append(lista[j])

#Se ponen lado a lado todos los valores que son moda
valores= str(nums[0])
for i in range(1, len(nums)):
    valores= valores + "," + str(nums[i])

print(f"El/los numero(s) moda es/son {valores}, repetido(s) {moda} veces en la lista")
n= int(input("Ingrese el numero de elementos de la lista: "))

lista= []

print(f"Ingrese los {n} valores de la lista: ")
for i in range(n):
    e= int(input())
    lista.append(e)
print(f"Su lista es de la forma {lista}")

conteos = []

for i in range(len(lista)):
    conteo = 0
    for j in range(len(lista)):
        if lista[j] == lista[i]:
            conteo = conteo + 1
    conteos.append(conteo)

moda= conteos[0]
num= lista[0]
for i in range(1, len(conteos)):
    if conteos[i]>moda:
        moda= conteos[i]
        num= lista[i]

nums= []
for j in range(len(lista)):
    if conteos[j]==moda:
        rep= False
        for k in range(len(nums)):
            if lista[j]== nums[k]:
                rep= True
        if rep== False:
            nums.append(lista[j])

fe= str(nums[0])
for i in range(1, len(nums)):
    fe= fe + "," + str(nums[i])

print(f"El/los numero(s) moda es/son {fe}, repetido(s) {moda} veces en la lista")
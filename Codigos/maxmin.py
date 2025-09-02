import random as rnd

n = 10
lista = []
for i in range(n):
    lista.append(rnd.randint(1,100))

print(lista)

max = lista[0]
posmax = 0
for i in range(n):
    if lista[i] > max :
        max = lista[i]
        posmax = i

print(f"el maximo es {max}, en la posición {posmax}")

min = lista[0]
posmin = 0
for i in range(n):
    if lista[i] < min :
        min = lista[i]
        posmin = i

print(f"el minimo es {min}, en la posición {posmin}")
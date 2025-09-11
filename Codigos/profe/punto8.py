import random as rnd

n = 20
lista = []
for i in range(n):
    lista.append(rnd.randint(0, 100))
print(lista)

conteos = []
for i in range(n):
    conteo = 0 # veces que aparece el elemento lista[i]
    for j in range(n):
        if lista[i] == lista[j] :
            conteo = conteo + 1
    conteos.append(conteo)

print(lista)
print(conteos)

maxi = 0
max = conteos[0]

for i in range(n) :
    if conteos[i] > max :
        max = conteos[i]
        maxi = i 
        
print(f"la moda es {lista[maxi]}")
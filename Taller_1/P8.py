import random as rnd

n = int(input("Numero de elementos de la lista: "))
a = int(input("limite inferior (enteros): "))
b = int(input("limite superior (enteros): "))

lista = []
for i in range(n):
    lista.append(rnd.randint(a, b))
print(lista)
""""elementos = []
#for i in range(a, b + 1):
#    elementos.append(i)
elementos = [*range(a, b + 1)]

conteos = []

print(lista)


for j in range(len(elementos)):
    conteo = 0
    for i in range(n):
        if lista[i] == elementos[j] :
            conteo = conteo + 1
    conteos.append(conteo)

print(elementos)
print(conteos)

for i in range(len(elementos)):
    print(f"{elementos[i]} aparece {conteos[i]} veces")
conteo=0

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i]==lista[j]:
            conteo= conteo + 1
    print(conteo)
    conteo= 0"""
menor= lista[0]
for j in range(lista[1], lista[len(lista)-1]+1):
    if lista[j]>lista[0]:
        menor= lista[i]
a= menor
print(a)
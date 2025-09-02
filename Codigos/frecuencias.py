import random as rnd

n = int(input("Numero de elementos de la lista: "))
a = int(input("limite inferior (enteros): "))
b = int(input("limite superior (enteros): "))

lista = []
for i in range(n):
    lista.append(rnd.randint(a, b))

elementos = []
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
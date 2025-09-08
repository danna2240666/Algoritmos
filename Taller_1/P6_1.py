n= int(input("Ingrese el numero de elementos de la lista: "))

lista= []

print(f"Ingrese los {n} valores de la lista: ")
for i in range(n):
    num= int(input(f"{i+1}. "))
    lista.append(num)
print(f"La lista es de la forma {lista}")

suma= 0
div= 0

for i in range(len(lista)):
    if lista[i]%2== 0:
        suma= suma + lista[i]
        div= div + 1
print(f"La media de los valores pares de la lista es {suma/div}")


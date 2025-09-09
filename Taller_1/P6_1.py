#Version con listas

n= int(input("Ingrese el numero de elementos de la lista: "))

lista= []

#Se pide un n numero de inputs y se agregan a una lista
print(f"Ingrese los {n} valores de la lista: ")
for i in range(n):
    num= int(input(f"{i+1}. "))
    lista.append(num)

suma= 0
div= 0

for i in range(len(lista)):
    #Si el residuo del numero dividido en 2 es cero, es par y se suman todos
    if lista[i]%2== 0:
        suma= suma + lista[i]
        #Cuenta la cantidad de numeros pares
        div= div + 1

#suma/div es la media de los numeros pares de la lista
print(f"La media de los valores pares de la lista es {suma/div}")


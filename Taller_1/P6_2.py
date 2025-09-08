n= int(input("Ingrese el numero de elementos a tener en cuenta: "))

print(f"Ingrese los {n} valores de la lista: ")

suma= 0
div= 0

for j in range(n):
    num= int(input(f"{j+1}. "))
    if num%2==0:
        suma= suma + num
        div= div +1
print(f"La media de los valores pares es {suma/div}")
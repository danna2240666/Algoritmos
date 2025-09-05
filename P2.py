n= int(input("Ingrese el valor para comprobar si tiene raiz entera: "))

i=1
while n!=i**2:
    if i==n:
        print(f"{n} no tiene una raiz entera")
        break
    i= i+1
else:
    print(f"{n} tiene raiz entera {i}")
n= int(input("Ingrese el valor para comprobar si tiene raiz exacta: "))

k=1
for i in range(1,n):
    if n==i**2:
        k=0
if k==0:
    print("raiz exacta")
else:
    print("no")

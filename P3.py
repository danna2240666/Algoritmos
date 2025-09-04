n= int(input("Ingrese el numero a representar en base b: "))
b= int(input("Ingrese la base b: "))

if b>9:
    print("Por favor ingrese un valor entre 1 y 9")

d= n/b
r= n%b

L= []

while d>1:
    L.append(r)
    d=d/b
    r=d%b
print(L)

n= int(input("Ingrese el numero a representar en base b: "))
b= int(input("Ingrese la base b: "))

if b>9:
    print("Por favor ingrese un valor entre 1 y 9")

d= n

suma= ""

for i in range(1, n+1):
    if d>1:
        d= int(d/b**i)
        r= str(d%b)
        suma= r + suma
    elif d==1:
        suma= "1" + suma
        print(suma)
    else:
        print(suma + "f")
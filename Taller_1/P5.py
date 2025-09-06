n= input("Ingrese el numero a cambiar: ")

suma= n[len(n)-1]

for i in range(len(n)-2, -1, -1):
    suma= n[i] + "0" + suma
print(suma)
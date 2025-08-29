n = int(input("Ingrese el limite de la suma: "))
a = float(input("Ingrese el incio del intervalo: "))
b = float(input("Ingrese el final del intervalo: "))

suma = 0
for i in range(0,n):
    suma= suma + ((a+i*(b-a)/n)**2)*(b-a)/n
print(suma)

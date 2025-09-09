n= int(input("Ingrese el numero para hallar el primo mas cercano: "))

conteo= 0

for i in range(2,n+1):
    conteo= 0
    for j in range(2, i):
        if i%j==0:
            conteo= conteo +1
    if conteo== 0:
        primo= i
print(f"El primo mas cercano menor/igual a {n} es {primo}")

conteo=0
k= n+1
while n<k:
    for j in range(2, k):
        if k%j==0:
            conteo= conteo + 1
    if conteo==0:
        print(f"El primo mas cercano mayor a {n} es {k}")
        k=0
    else:
        conteo= 0
        k= k +1
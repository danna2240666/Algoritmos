n = int(input("n?: "))
pares = 0

suma = 0
suma2 = 0
for i in range(n) :
    elem = float(input(f"elemento {i}: "))
    if elem % 2 == 0 :
        suma = suma + elem
        suma2 = suma2 + elem ** 2        
        pares = pares + 1
        
if pares > 0 :
    res = suma2 / pares - (suma ** 2) / (pares ** 2)
    print(res ** (1/2))
else :
    print("No hubo pares / puros impares")       
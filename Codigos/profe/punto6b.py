n = int(input("n?: "))
pares = 0

suma = 0
for i in range(n) :
    elem = float(input(f"elemento {i}: "))
    if elem % 2 == 0 :
        suma = suma + elem
        pares = pares + 1
        
if pares > 0 :
    print(suma/pares)
else :
    print("No hubo pares / puros impares")        
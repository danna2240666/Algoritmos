n = int(input("n?: "))
lista = []
pares = 0
for i in range(n) :
    lista.append(float(input(f"elemento {i}: ")))

suma = 0
for i in range(len(lista)) :
    if lista[i] % 2 == 0 :
        suma = suma + lista[i]
        pares = pares + 1
        
if pares > 0 :
    print(suma/pares)
else :
    print("No hubo pares / puros impares")        
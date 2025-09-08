n= input("Ingrese la frase a reflejar: ")

suma= ""

for i in range(len(n)):
    suma= n[i] + suma
print(suma)

frase= n.split()
reves= ""

for j in range(len(frase)):
    orden= ""
    for k in range(len(frase[j])):
        orden= (frase[j])[k] + orden
    reves= reves + orden + " "

print(reves)

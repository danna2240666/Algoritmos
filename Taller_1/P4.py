n= input("Ingrese la frase a reflejar: ")

suma= ""

#Este loop refleja la frase como un espejo
for i in range(len(n)):
    #Una string se puede ver como una lista de letras con posicion n[i]
    suma= n[i] + suma
print("-->", suma)

#Cada palabra se vuelve elemento de una lista
frase= n.split()
reves= ""

#Este loop mantiene el orden de las palabras, pero refleja las letras de cada una
for j in range(len(frase)):
    orden= ""
    #Loop para reflejar las letras
    for k in range(len(frase[j])):
        orden= (frase[j])[k] + orden
    #Organiza las palabras de izquierda a derecha
    reves= reves + orden + " "

print("-->", reves)

frase = input(": ")
palabras = frase.split(" ")
frase_v = ""
print(palabras)
for i in range(len(palabras)):
    pal_v = ""
    pal = palabras[i]
    for j in range(len(palabras[i])):
        pal_v = pal[j] + pal_v 
    frase_v = frase_v + " " + pal_v
print(frase_v)

frase_v = ""
for j in range(len(frase)):
    frase_v = frase[j] + frase_v 
print(frase_v)
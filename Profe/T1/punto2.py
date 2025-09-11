n = int(input("Numero a revisar: "))
raiz = n ** (1/2)
print(raiz)
if raiz == int(raiz) :
    print("Cuadrado perfecto")
else :
    print("No cuadrado perfecto")
    
i = 1   
detecto = False 
while i <= n :
    if i * i == n :
        print("Cuadrado perfecto")
        detecto = True
    i = i + 1
if detecto == False :
    print("No cuadrado perfecto")            

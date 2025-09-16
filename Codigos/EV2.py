#Se pide el limite hasta donde se calcularan los numeros con raiz entera
n = int(input("Ingrese el limite de la suma: "))

#Si no hay numeros con raiz entera en el rango, la suma sera 0, si no, sera el valor inicial de la suma mas adelante
suma= 0

for i in range(1, n+1):
    #Se calcula el valor de la raiz de todos los numeros en el rango
    raiz = i**(1/2)
    #Si su raiz es un entero, entonces cumple la condicion que se busca y se agrega a la sumatoria
    if raiz == int(raiz) :
        suma= suma + i
print(f"La suma de los numeros con raiz entera es igual a {suma}")
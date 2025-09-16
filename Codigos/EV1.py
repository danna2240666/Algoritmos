n= int(input("Ingrese el numero para hallar los numeros primos mas cercanos: "))

primos= []

#Se pone un condicion para que el valor que se de sea mayor que 2"
if n<=2:
    print("Por favor ingrese un numero mayor a 2")
    
else:
    #Con este loop se calculan todos los numeros primos hasta n
    for i in range(2,n+1):
        conteo= 0
        for j in range(2, i):
            #Si el numero es divisible entre cualquier valor del rango, se aumenta el valor de los divisores de este numero
            #El range no tiene en cuenta al 1 y al mismo numero ya que esos son los unicos divisores de los primos
            if i%j==0:
                conteo= conteo +1
        #Si al final este numero no cuenta con ningun divisor aparte de 1 y si mismo, se agrega a una lista con todos los primos hasta n
        if conteo== 0:
            primos.append(i)
    #Se muestran los dos ultimos valores de la lista de primos ya que se van guardando en orden, asi que estos seran los mas cercanos a n
    print(f"Los dos numeros primos mas cercanos menores o igual a {n} son {primos[len(primos)-2]} y {primos[len(primos)-1]}")
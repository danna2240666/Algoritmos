#Version sin listas

n= int(input("Ingrese el numero total de datos: "))

suma_cuadrados=0
suma_valores= 0

#Si expandimos la formula de sumatoria (x-media)^2, obtenemos que la desviacion estandar tambien se puede escribir como
#sumatoria de cada valor elevado al cuadrado sobre n, menos la sumatoria de todos los valores elevada al cuadrado sobre n^2

print(f"Ingrese los {n} valores de la lista: ")
#Con la formula reescrita, no necesitamos una lista para utilizar los valores luego, solo hacer las sumatorias correspondientes
for i in range(n):
    num= int(input(f"{i+1}. "))
    suma_cuadrados= suma_cuadrados + num**2 #sumatoria de cada valor elevado al cuadrado
    suma_valores= suma_valores + num #sumatoria de todos los valores

desviacion= (suma_cuadrados/n)-(((suma_valores)**2)/n**2)

print(f"La desviacion estandar de los datos es {(desviacion)**(1/2)}")
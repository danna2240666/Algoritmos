import math
print("""Escoja el numero de alguna de las siguientes opciones
1. Seno
2. Coseno
3. Tangente
4. Salir
  """)

op= int(input("Su selección: "))

#Se detiene el programa si se da la opcion de salir y se restringe una respuesta mayor a 4
if op == 4:
    exit()
if op > 4:
   print("Por favor escoger un numero entre 1 y 4")

r= float(input("Ingrese el argumento x de la funcion: "))
n= int(input("Ingrese el limite n de la serie (n < 17): "))

#El limite n se utiliza para calcular un factorial, si se usar un valor mayor que 16, el programa no lo puede calcular
#Por esto se crea una restriccion para que no salga un error
if n>16:
   print("Por favor escoger un limite menor que 17")
   exit()

#Se convierten de grados a radianes y se pone un valor inicial para las sumatorias y el factorial
x= r*(math.pi)/180
factorial= 1
sin= 0
cos= 0

#Para cada opcion se sigue un calculo distinto
if op == 1:
    #Con este loop se calcula el factorial
    for i in range(n+1):
      for j in range(1, 2*i+2):
         factorial= factorial*j
      #Teniendo ese valor se procede a usar la formula para aproximar el seno, siendo i cada valor de 0 a 16
      sin = sin + ((-1)**i)*(x**(2*i+1))/(factorial)
    print(sin)

#El calculo del seno es similar al del seno
elif op == 2:
    for i in range(n+1):
      for j in range(1, 2*i+1):
         factorial= factorial*j
      cos= cos + ((-1)**i)*(x**(2*i))/(factorial)
    print(cos)
else:
   print("El valor de esta opcion se puede hallar, pero aun no ha sido implementada")

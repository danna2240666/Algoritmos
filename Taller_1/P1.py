import math
print("""Escoja el numero de alguna de las siguientes opciones
1. Seno
2. Coseno
3. Tangente
4. Salir
  """)

op= int(input("Su selección: "))

if op == 4:
    exit()
if op > 4:
   print("Por favor escoger un numero entre 1 y 4")

r= float(input("Ingrese el argumento x de la funcion: "))
n= int(input("Ingrese el limite n de la serie (n < 17): "))

x= r*(math.pi)/180
num= 1
sin= 0
cos= 0

if op == 1:
    for i in range(n+1):
      for j in range(1, 2*i+2):
         num= num*j
      sin = sin + ((-1)**i)*(x**(2*i+1))/(num)
    print(sin)
elif op == 2:
    for i in range(n+1):
      for j in range(1, 2*i+1):
         num= num*j
      cos= cos + ((-1)**i)*(x**(2*i))/(num)
    print(cos)
else:

   print("El valor de esta opcion se puede hallar, pero aun no ha sido implementada")

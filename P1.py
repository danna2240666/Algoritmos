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
n= int(input("Ingrese el limite de la serie: "))

x= r*180*(math.pi)
num=1

if op == 1:
    for i in range(n+1):
      for j in range(1, 2*i+1):
         num= num*j
      sin= ((-1)**i)*(x**(2*i+1))/(num)
    print(sin)
elif op == 2:
    for i in range(n+1):
      cos= ((-1)**i)*(x**(2*i))/(2*i)
    print(cos)
else:
   print("mensaje")
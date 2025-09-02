print("""Escoja el numero de alguna de las siguientes opciones
1. Seno
2. Coseno
3. Tangente
4. Salir
  """)
op= int(input("Su selección: "))

if op == 4:
    exit()

r= float(input("Ingrese el argumento x de la funcion: "))
n= int(input("Ingrese el limite de la serie: "))

x= r*180

if op == 1:
    for i in range(n+1):
      sin= ((-1)**i)*(x**(2*i+1))/(2*i+1)
    print(sin)
elif op == 2:
    for i in range(n+1):
      cos= ((-1)**i)*(x**(2*i))/(2*i)
    print(cos)
else:
   print("mensaje")
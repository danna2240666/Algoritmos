#Version con listas

n= int(input("Ingrese el numero total de datos: "))

lista= []
media= 0
desviacion= 0

print(f"Ingrese los {n} valores de la lista: ")
for i in range(n):
    #Se piden n inputs y se utiliza el loop para dividir el numero sobre n y hacer la sumatoria
    num= int(input(f"{i+1}. "))
    media= media + num/n
    lista.append(num)

for i in range(n):
    desviacion= desviacion + ((lista[i]-media)**2)/n

print(f"La desviacion estandar de los datos es {(desviacion)**(1/2)}")
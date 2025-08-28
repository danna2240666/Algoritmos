import random as rnd
C = []
n = 100
a = int(input("a: "))
b = int(input("b: "))
for i in range(n):
    C.append(rnd.randint(a,b))
print(C)

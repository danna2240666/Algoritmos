import random as rnd
C = []
n = 100
a = int(input("a: "))
b = int(input("b: "))
for i in range(n):
    C.append(rnd.randint(a,b))
print(C)
conti= 0
for k in range(a,b+1):
    for i in range(n):
        if C[i] == k:
            conti= conti + 1
            print(conti)
m = int(input("limte: "))

n = 1
uprimo = 0
while n <= m:
    divisores = 0
    for i in range(2, n):
        if n % i == 0:
            divisores = divisores + 1
    if divisores <= 0 :
        uprimo = n
    n = n + 1
print(uprimo)

m = int(input("limte: "))

n = m
uprimo = 0
while uprimo == 0 :
    divisores = 0
    for i in range(2, n):
        if n % i == 0:
            divisores = divisores + 1
    if divisores <= 0 :
        uprimo = n
    else :
        n = n + 1
    
print(uprimo)
n = int(input("n?: "))

res = 0
factor = 1
while n > 0 :
    r = n % 10
    n = n // 10
    res = res + r * factor
    factor = factor * 10000
print(res)

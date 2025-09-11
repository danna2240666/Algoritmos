n = int(input("n?: "))
b = int(input("b?: "))

if b >= 10 or b < 0 :
    print("No se puede")
else :
    nb = 0
    factor = 1
    while n > 0 :
        r = n % b
        n = n // b
        print(r)
        nb = nb + r * factor
        factor = factor * 10
    print(nb)
        
    
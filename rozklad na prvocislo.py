def delitel(n):
    deli = 2
    while n != 1:
        if n % deli == 0:
            n = n //deli
            print(deli,end=",")
        else:
            deli += 1



delitel(12)
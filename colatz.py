def colatz(n):
    while n != 1:
        if n % 2 == 0:
            n //= 2
            print(n, end=',')
        else:
            n = 3*n + 1
            print(n, end=",")
    print()
for i in range(1,101):
    colatz(i)


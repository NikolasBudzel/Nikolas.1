def fak(n):
    x = 1
    for i in range(n, 1, -1):
        x = x*i
    return x

print(fak(5))
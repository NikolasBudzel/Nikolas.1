def sucet(z,k):
    spl = sum(i for i in range(z, k+1)if i % 2 == 1)
    return spl
print(sucet(6,10))
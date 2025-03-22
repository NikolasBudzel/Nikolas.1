def faktorial(n):
    vysledok = 1
    for i in range(1,n+1):
        vysledok = vysledok*i
    return vysledok

def ludolf(k):
    zoznam = []
    vysledok = 0
    for i in range(0,k):
        ramanujan = (faktorial(4*i)*(1103+26390*i))/((faktorial(i)**4)*(396**(4*i)))
        vysledok += ramanujan
        zoznam.append(1/(((2*2**0.5)/9801)*vysledok))
    return zoznam
print(ludolf())


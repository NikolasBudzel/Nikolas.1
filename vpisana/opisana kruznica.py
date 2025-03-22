import math as m
def polomer_vpisana(a,b,c):
    o = a+b+c
    s = o/2
    S = ((s-a)*(s-b)*(s-c)**0.5)
    r = (2*S)/o
    return r

def polomer_opisana(a,b,c):
    beta = m.degrees(m.acos((-b**2+a**2+c**2)/(2*a*c)))
    r = a/(2*m.sin(beta))
    return r

print(polomer_opisana(6,5,8))
print(polomer_vpisana(6,5,8))
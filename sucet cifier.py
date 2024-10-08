def sucet_cifier(cislo):
    cifra = 0
    while cislo > 0:
        ld = cislo % 10
        #spocitanie parnych
        if ld % 2 == 0:
            cifra += ld
        cislo = cislo // 10
    return cifra

print(sucet_cifier(125))

def cislo_odzadu(cislo):
    cifra = 0 # inicializovali sme  premennu s hodnotou nula
    while cislo > 0:
        ld = cislo % 10
        cifra = cifra*10 + ld # cislo odzadu
        cislo = cislo // 10
    return cifra

print(sucet_cifier(125))
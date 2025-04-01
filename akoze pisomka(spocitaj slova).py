fr = open("slova.txt", "r")
def pocitadlo():
    pocitadlo = 0
    for riadok in fr:
        riadok = riadok.strip()
        if (riadok[0] == "c" or riadok[0] == "t") and (riadok[-1] == "e" or riadok[-1] == "a"):
            pocitadlo += 1
    print(pocitadlo)

def palindrom_pocet():
    pocet = 0
    for row in fr:
        row = row.strip()
        if row[::-1] == row:
            pocet +=1
    print(pocet)


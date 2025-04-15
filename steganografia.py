#ak je parne bude koncit nulou
#kodujeme spravu do  zmeny modrej farby
sprava = input("zadaj spravu: ")
def kodovacka(sprava):
    sifrovana =[]
    for i in sprava:
        bin_znak = bin(ord(i))[2::] #vieme pouzit: binznak = format(ord(i), "08b")
        if len(bin_znak) < 8:
            plus_nuly = (8-len(bin_znak))*"0" + bin_znak
        for j in plus_nuly:
            sifrovana.append(int(j))
    return sifrovana

print(kodovacka(sprava))
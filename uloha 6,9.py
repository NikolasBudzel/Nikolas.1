def poc_cif(n):
    poc = 0
    while n !=0:
        poc = poc + 1
        n = n // 10
    return poc

def shredder(n):
    if poc_cif(n) % 2 == 0:
        pozicia = poc_cif(n) // 2
        sucet = 0
        poc = 0
        while n!=0:
            poc = poc + 1
            if poc == pozicia or poc == pozicia - 1:
                sucet = sucet + n % 10
            n = n // 10
        return sucet
    else:
        pozicia = poc_cif(n) // 2
        sucet = 0
        poc = 0
        while n != 0:
            poc = poc + 1
            if poc == pozicia+1:
                sucet = sucet + n % 10
            n = n // 10
        return sucet
print(shredder(3939639393939939393))
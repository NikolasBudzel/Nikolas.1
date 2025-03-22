def je_usporiadana(zoznam1):
    for i in range(0, len(zoznam1)-1):
        if zoznam1[i+1]<zoznam1[i]:
            return False
    return True

def rovnake_hodnoty(zoznam2):
    if zoznam2.count(zoznam2[0]) == len(zoznam2):
        return True
    else:
        return False

    for i in range(0,len(zoznam2)-1):
        if zoznam2[i] != zoznam2[i+1]:
            return False
    return True


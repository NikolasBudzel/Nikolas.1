def uloha1_vypocet_cifer_suctu(retazec):
    sucet = 0
    for i in retazec:
        sucet += int(i)
    return sucet

def uloha2_pocet_samohlasok(retazec):
    samohlasky = "aeiouy"
    for i in samohlasky:
        print(f"Samohlaska {i} sa tam nachadza {retazec.count(i)}")

def uloha3_zatvorky(retazec):
    zaciatok = retazec.find("(")
    koniec = retazec.find(")")
    if (koniec- zaciatok > 0):
        vysledok = retazec[zaciatok+1:koniec]
        print(vysledok)

def uloha4_opakuj(retazec):
    while retazec.find("(") != -1:
        uloha3_zatvorky(retazec)
        zaciatok = retazec.find("(")
        koniec = retazec.find(")")
        retazec = retazec[:zaciatok:]+retazec[koniec+1::]

def uloha7_odstran_samohlasky(retazec):
    samohlasky = "aeiouy"
    novy = ""
    for i in retazec:
        if i not in samohlasky:
            novy += i
    return novy

def uloha8_opyt_oznam_rozkaz(retazec):
    print(f"rozkaz: {retazec.count("!")}")
    print()



def uloha9_pocet_samohlasky_spoluhlasky(retazec):
    samohlasky = "aeiouy"
    spoluhlasky = "qwrtpsdfghjklzxcvbnm"
    pocet_samohlasky = 0
    pocet_spoluhlasky = 0
    for i in retazec:
        if i in samohlasky:
            pocet_samohlasky += 1
        if i in spoluhlasky:
            pocet_spoluhlasky += 1
    print(f"spoluhlasok je: {pocet_spoluhlasky}, samohlasok je: {pocet_samohlasky}")

def uloha10_urci_priponu(retazec:str):
    zaciatok = retazec.rfind(".")
    pripona = retazec[zaciatok+1::]
    if pripona == "txt" or pripona == "docx" or pripona == "py" or pripona == "pdf":
        print("text dokument")
    elif pripona == "xlsx":
        print("tabulka")
    elif pripona == "img":
        print("obrazok")

def uloha11_vsetky_4miestne_PIN():
    pin = "0123"
    for i in pin:
        for j in pin:
            for k in pin:
                for l in pin:
                    print(i,j,k,l)

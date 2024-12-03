def cezarova_sifra(input:str,offset:int):
    output = ""
    for char in input:
        if(97<=ord(char) and ord(char)<=122):
            output += chr((ord(char) - 97 + offset) % 26 + 97)
    return output

def desifruj(input:str,offset:int):
    output = ("")
    for char in input:
        if (97 <= ord(char) and ord(char) <= 122):
            output += chr((ord(char) - 97 - offset) % 26 + 97)
    return output

def predlz_kluc(retazec,kluc):
    kolko = len(retazec)//len(kluc)
    zvysok = len(retazec)%len(kluc)
    return kluc*kolko+kluc[:zvysok:]
def sifra ():
    kluc = input("zadaj kluc: ")
    retazec = input("zadaj rezatec: ")
    ret1 = predlz_kluc(retazec,kluc)
def
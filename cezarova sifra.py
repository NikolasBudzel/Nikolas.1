# def cezarova_sifra(input:str,offset:int):
#     output = ""
#     for char in input:
#         if(97<=ord(char) and ord(char)<=122):
#             output += chr((ord(char) - 97 + offset) % 26 + 97)
#     return output
#
# def desifruj(input:str,offset:int):
#     output = ("")
#     for char in input:
#         if (97 <= ord(char) and ord(char) <= 122):
#             output += chr((ord(char) - 97 - offset) % 26 + 97)
#     return output
#
# def predlz_kluc(retazec,kluc):
#     kolko = len(retazec)//len(kluc)
#     zvysok = len(retazec)%len(kluc)
#     return kluc*kolko+kluc[:zvysok:]
#
# def sifra ():
#     kluc = input("zadaj kluc: ")
#     retazec = input("zadaj rezatec: ")
#
#     ret1 = predlz_kluc(retazec,kluc)
#


def cezarova_sifra_retazec(text:str,key:str):
    result = ""
    for i, char in enumerate(text):
        if char.isascii():
            if (ord(char) >= ord("a") and ord(char) <= ord("z")):
                is_upper = char.isupper()
                is_space = char == " "
                char = char.lower()
                shift = ord(key[i % len(key)].lower()) - ord('a')
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                if is_upper:
                    shifted_char = shifted_char.upper()
                    result += shifted_char
            else:
                result += char
        else:
            result += char
    return result

def predlz_kluc(retazec,kluc):
    kolko = len(retazec)//len(kluc)
    zvysok = len(retazec)%len(kluc)
    return kluc*kolko+kluc[:zvysok:]

def cezar_retazec ():
    retazec = input("zadaj rezatec: ")
    kluc = input("zadaj kluc: ")
    predlzenz_kluc = predlz_kluc(retazec, kluc)
    zasifrovany_text = cezarova_sifra_retazec(retazec, predlzenz_kluc)
    return zasifrovany_text

print(cezar_retazec())

# fr = open("text.txt", "r", encoding="utf-8")
# ##sposoby ako pracovat s obsahom suboru
# for riadok in fr:
#     print(riadok, end="")
#     ## print(riadok.strip(), end=".\n")
#
# ##inak prvy riadok a inak zyvsok
# prvy_riadok = fr.readline()
# print(prvy_riadok)
# for riadok in fr:
#     print(riadok)
#
# ##zoznam
# zoznam = fr.readlines()
# print(zoznam)

fr = open("D:\škola\Downloads\slova.txt","r",encoding="utf-8")
conter = 0
for riadok in fr:
    if riadok.count("e") >= 1:
        conter += 1
print(conter)
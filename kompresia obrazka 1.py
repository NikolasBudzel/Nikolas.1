fr = open("kompresia_obrazka_1.txt", "r")
fw = open("kompresia_obrazka_vystup.txt", "w")

def spracuj_riadok(row):
    vystup = ""
    if row[0] == "1":
        vystup+="0"+ " "
    pocitadlo = 1
    for index in range(1, len(row)):
        if row[index]==row[index-1]:
            pocitadlo+=1
        else:
            vystup+=(str(pocitadlo)+" ")
            pocitadlo = 1
    vystup += str(pocitadlo)
    fw.write(vystup+"\n")


first_line = fr.readline()
fw.write(first_line)
sirka,dlzka = first_line.strip().split(" ") # su to stringy


for riadok in fr:
    spracuj_riadok(riadok.strip())
fw.close()


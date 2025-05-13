from PIL import Image
fr = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8")
prvy_riadok = fr.readline()
sirka, vyska = prvy_riadok.strip().split()
sirka = int(sirka)
vyska = int(vyska)

obrazok = Image.new("RGB", (sirka, vyska), (255,255,255))
mapa_pixelov = obrazok.load()
y = 0
for riadok in fr:#prechadzam subor po riadkoch
    temp = riadok.strip()#odstrani enter
    for x in range(0, len(temp), 2):#prechadzame riadok po dvoch(16kova sustava)
        print(temp[x:x+2])
        jozo = int(temp[x:x+2],16)
        mapa_pixelov[x//2, y] = (jozo, jozo,jozo)
    y+=1

obrazok.show()
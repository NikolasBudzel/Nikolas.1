from PIL import Image


def sachovnica(sirka,vyska):
    obrazok = Image.new("RGB", (sirka, vyska), (255, 255, 255))
    mapa_pixelov = obrazok.load()
    for y in range(vyska):
        for x in range(sirka):
            if (x+y) % 2 == 0:
                mapa_pixelov[x,y] = (0,0,0)
    obrazok.show()

def diagonaly(sirka,vyska):
    obrazok = Image.new("RGB", (sirka, vyska), (255, 255, 255))
    mapa_pixelov = obrazok.load()
    for y in range(vyska):
        for x in range(sirka):
            if x == y:
                mapa_pixelov[x,y] = (0,0,255)
            if (x+y+1) == sirka:
                mapa_pixelov[x,y] = (255,0,0)
    obrazok.show()

def karovane(sirka,vyska):
    obrazok = Image.new("RGB", (sirka, vyska), (255, 255, 255))
    mapa_pixelov = obrazok.load()
    for y in range(vyska):
        for x in range(sirka):
            if x%2==0 and y%2==0:
                mapa_pixelov[x,y] = (0,0,255)
            else:
                mapa_pixelov[x,y] =(0,2,3)
    obrazok.show()

def okienka(sirka,vyska):
    obrazok = Image.new("RGB", (sirka, vyska), (255, 255, 255))
    mapa_pixelov = obrazok.load()
    for y in range(vyska):
        for x in range(sirka):
            if

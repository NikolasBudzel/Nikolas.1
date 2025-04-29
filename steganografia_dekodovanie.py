from PIL import Image

def dekodovacka(menosuboru="salka0.png"):
    img = Image.open(menosuboru)
    sirka,vyska = img.size
    pixels = img.load()

    sprava = ""
    for y in range(vyska):
        for x in range(sirka):
            pixel = pixels[x,y][2]
            bin_pixel = bin(pixel)
            posledny_znak = bin_pixel[-1]
            sprava += posledny_znak

            if len(sprava) == 8:
                pismeno = chr(int(sprava,2))
                if pismeno == "#":
                    return
                sprava = ""
                print(pismeno,end="")

dekodovacka("vystup (1).png")
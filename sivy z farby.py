from PIL import Image

obr = Image.open("vodales.jpg")
sirka,vyska = obr.size
obr_sivy = Image.new("RGB", (sirka,vyska),(255,255,255))
obr_cerveny = Image.new("RGB", (sirka,vyska),(255,255,255))
obr_zeleny = Image.new("RGB", (sirka,vyska),(255,255,255))
obr_modry = Image.new("RGB", (sirka,vyska),(255,255,255))
pixels = obr.load()
pixels_sivy = obr_sivy.load()
pixels_cerveny = obr_cerveny.load()
pixels_zeleny = obr_zeleny.load()
pixels_modry = obr_modry.load()
for y in range(vyska):
    for x in range(sirka):
        avg = sum(pixels[x,y])//3
        pixels_sivy[x,y]=(avg,avg,avg)
        pixels_cerveny[x,y]=(pixels[x,y][0],0,0)
        pixels_zeleny[x,y]=(0,pixels[x,y][0],0)
        pixels_modry[x,y]=(0,0,pixels[x,y][0])

obr_sivy.show()
obr_cerveny.save("obr_cerveny.jpg")
obr_zeleny.save("obr_zeleny.jpg")
obr_modry.save("obr_modry.jpg")
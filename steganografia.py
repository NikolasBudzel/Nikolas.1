from PIL import Image

img = Image.open("sisapo_ciudad_romana_la bienvenida_ciudad_real_55.png")
sirka,vyska = img.size
pixels = img.load()


#ak je parne bude koncit nulou
#kodujeme spravu do  zmeny modrej farby
sprava = input("zadaj spravu: ")

def kodovacka(sprava):
    global kompletka
    sifrovana = []
    for i in sprava:
        bin_znak = format(ord(i), "08b") #vieme pouzit: binznak = format(ord(i), "08b")
        if len(bin_znak) < 8:
            plus_nuly = 8-len(bin_znak)
            kompletka = plus_nuly * "0" + bin_znak
        else:
            kompletka = bin_znak
        for j in kompletka:
            sifrovana.append(int(j))
    return sifrovana

def drticka(sprava):
    bin_sprava = kodovacka(sprava)
    for i in range(len(bin_sprava)):
        x = i % int(sirka)
        y = i // int(sirka)
        modry_pixel = pixels[x,y][2]
        bin_modry_pixel = bin(modry_pixel)
        zakodovany_pixel = bin_modry_pixel[2:-1:]+str(bin_sprava[i])
        zakodovany_pixel_final = int(zakodovany_pixel,2)
        pixels[x,y] = (pixels[x,y][0],pixels[x,y][1],zakodovany_pixel_final)
    img.save("kodovane.png")

drticka(sprava)

#Mount Whymper is a 2,845-metre-high (9,334 ft) mountain located in the Canadian Rockies in the Canadian province of British Columbia. Located in the Vermilion Pass in Kootenay National Park, it is named after Edward Whymper, who, along with four guides (Joseph Bossoney, Christian Kaufmann, Christian Klucker, and Joseph Pollinger), was the first to climb the mountain in 1910. Mount Whymper is composed of sedimentary rock laid down during the Precambrian to Jurassic periods as part of the Laramide orogeny. This panoramic photograph shows the southeastern aspect of Mount Whymper, as seen from the Stanley Glacier Trail, with Stanley Valley in the foreground.#

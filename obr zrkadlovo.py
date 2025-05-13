from PIL import Image

img = Image.open("img.png")
sirka,vyska = img.size
pixels = img.load()

for y in range(vyska):
    for x in range(sirka):

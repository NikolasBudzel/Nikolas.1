from PIL import Image

img = Image.open("img.png")
sirka,vyska = img.size
pixels = img.load()

def make_gray(pixel:tuple):
    avg = (pixel[0] + pixel[1] + pixel[2]) // 3
    return (avg,avg,avg)

def diff_pixels(p1,p2):
    return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def add_pixels(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])

def multiply(p1,num):
    return (int(p1[0]*num), int(p1[1]*num), int(p1[2]*num))

for y in range(1, vyska - 1):
    for x in range(1, sirka - 1):
        oldpixel = pixels[x,y]
        newpixel = make_gray(oldpixel)
        pixels[x,y] = newpixel
        difference = diff_pixels(oldpixel,newpixel)
        pixels[x + 1,y] = add_pixels(pixels[x + 1,y], multiply(difference,7 / 16))
        pixels[x - 1,y + 1] = add_pixels(pixels[x - 1,y + 1] ,multiply(difference , 3 / 16))
        pixels[x,y + 1] = add_pixels(pixels[x,y + 1] , multiply(difference , 5 / 16))
        pixels[x + 1,y + 1] = add_pixels(pixels[x + 1,y + 1] , multiply(difference , 1 / 16))

img.show()
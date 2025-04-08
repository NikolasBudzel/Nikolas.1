from PIL import Image

fr = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8")
prvy_riadok = fr.readline()
sirka, vyska = prvy_riadok.strip().split()
sirka = int(sirka)
vyska = int(vyska)

obrazok = Image.new("RGB", (sirka, vyska), (255, 255, 255))
mapa_pixelov = obrazok.load()
y = 0
# #ak je vstupny subor v 10kovej sustave
# for riadok in fr:  # prechadzam subor po riadkoch
#     temp = riadok.strip().split()  # odstrani enter
#     for x in range(0, len(temp)):  # prechadzame riadok po dvoch(16kova sustava)
#         # print(temp[x:x + 2])
#         if temp[x] == "0":
#             mapa_pixelov[x, y] = (0,0,0)
#         else:
#             mapa_pixelov[x,y] = (255,255,255)
#     y += 1


# # ak je vstupny subor v 16kovej sustave
# for riadok in fr:
#     temp = riadok.strip()
#     for x in range(0, len(temp), 2):
#         hodnota = int(temp[x:x+2], 16)
#         if hodnota < 128:
#             mapa_pixelov[x // 2, y] = (0, 0, 0)
#         else:
#             mapa_pixelov[x // 2,y] == (255,255,255)
#     y += 1



obrazok.show()
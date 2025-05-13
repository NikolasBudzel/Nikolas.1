import random
import wave
fr = open("zvuky.txt", "r")
fl = fr.readline()
fr2 = open("zvuky2.txt", "r")
fl2 = fr2.readline()
menuet = []
trio = []
my_menuet = []
my_trio = []
for riadok in fr2:
    temporary = riadok.strip().split(" ")
    trio.append(temporary[1::])
#print(trio)
for riadok in fr:
    temporary = riadok.strip().split(" ")
    menuet.append(temporary[1::])
#print(menuet)
for i in range(16):
    my_menuet.append(menuet[random.randint(0,5)+random.randint(0,5)][i])

for i in range(16):
    my_trio.append(trio[random.randint(0,5)][i])

nahravky = ["takty/M"+ takt +".wav" for takt in my_menuet]
vystup = wave.open('nahodny_menuet.wav', 'wb')
nahravky1 = wave.open(nahravky[0])
vystup.setparams(nahravky1.getparams())

for i in range(len(nahravky)):
    nahravka = wave.open(nahravky[i], 'rb')
    vystup.writeframes(nahravka.readframes(nahravka.getnframes())) #[3]

vystup.close()
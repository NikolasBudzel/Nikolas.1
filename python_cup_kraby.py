import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=700, bg="white")
canvas.pack()

krab_0 = tk.PhotoImage(file="krab0.png")
krab_1 = tk.PhotoImage(file="krab1.png")
krab_2 = tk.PhotoImage(file="krab2.png")
krab_3 = tk.PhotoImage(file="krab3.png")
krab_4 = tk.PhotoImage(file="krab4.png")
krab_5 = tk.PhotoImage(file="krab5.png")

tl_rovnake = tk.PhotoImage(file="rovnake.png")
tl_rozne = tk.PhotoImage(file="rozne.png")

kraby = [krab_0 , krab_1, krab_2, krab_3, krab_4, krab_5]

krab_map = {
    1: "krab0.png",
    2: "krab1.png",
    3: "krab2.png",
    4: "krab3.png",
    5: "krab4.png",
    6: "krab5.png"
}

krab_map1 = {
    1: krab_0,
    2: krab_1,
    3: krab_2,
    4: krab_3,
    5: krab_4,
    6: krab_5
}

score = 0
score_pocet = tk.Label(root, text=f"score: {score}", font=("Arial", 18))
score_pocet.pack()

g_leftID = 0
g_rightID = 0

def zmena_obrazkov():
    ileft = random.randint(1,6)
    iright = random.randint(1,6)

    global g_leftID, g_rightID
    g_leftID = ileft
    g_rightID = iright

    print(krab_map[ileft],krab_map[iright])

    #l_krab = tk.PhotoImage(file=str(krab_map[ileft]))
    #r_krab = tk.PhotoImage(file=str(krab_map[iright]))

    #lavy = l_krab
    #pravy = r_krab

    #lavy = krab_map1[ileft]
    #pravy = krab_map1[iright]

    lavy = kraby[ileft-1]
    pravy = kraby[iright-1]

    #lavy = random.choice(kraby)
    #pravy = random.choice(kraby)

    tk.Label(root, image=lavy).place(x=100, y=100)
    tk.Label(root, image=pravy).place(x=400, y=100)


def isSAme():#pripocitavanie a odpocitavanie skore, pridat zmenu obrazkov
    global score
    if g_leftID == g_rightID:
        score += 1
    else:
        score += -10
    print(score)
    score_pocet.config(text=f"score: {score}", font=("Arial", 18))
    zmena_obrazkov()

def isNotSame():  # pripocitavanie a odpocitavanie skore, pridat zmenu obrazkov
    global score
    if g_leftID != g_rightID:
        score += 1
    else:
        score += -10
    print(score)
    score_pocet.config(text=f"score: {score}", font=("Arial", 18))
    zmena_obrazkov()


button1 = tk.Button(root, image=tl_rovnake, command=isSAme)
canvas.create_window(350,540,window=button1)
button1.image = tl_rovnake

button2 = tk.Button(root, image=tl_rozne, command=isNotSame)
canvas.create_window(350,600, window=button2)
button2.image = tl_rozne

zmena_obrazkov()

root.mainloop()
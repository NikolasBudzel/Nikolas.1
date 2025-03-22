import turtle
import tkinter as tk
import random

root = tk.Tk()
sirka = random.randint(100,400)
canvas = tk.Canvas(root, width=sirka, height=280)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

h=-(sirka/2)
t.penup()
t.goto(x=h+1,y=139)
t.pendown()
t.goto(x=-h-1,y=139)
t.goto(x=-h-1,y=-139)
t.goto(x=h+1,y=-139)
t.goto(x=h+1,y=139)

def troj(strana):
    t.pendown()
    t.forward(strana)
    t.left(120)
    t.forward(strana)
    t.left(120)
    t.forward(strana)
    t.left(120)
    t.forward(strana)
    t.penup()

# def riadok(y):
#     t.goto(x=h+1,y=y)
#     new_dlzka = 0
#     old_dlzka = 0
#     #print(sirka)
#     while sirka > new_dlzka:
#         dl = random.randint(20,80)
#         #print(f"increment to be extended:{dl}")
#         new_dlzka += dl
#         #print(f"kandidat dlzka napocitna:{new_dlzka,sirka}")
#         #print(f"som vo while")
#         if new_dlzka < sirka:
#             #print(f"som v if")
#             troj(dl)
#             old_dlzka += dl
#             #pozicia = t.xcor()
#     else:
#         nova_strana = sirka - old_dlzka   #dokreslim zvysny trojuholnik
#         troj(nova_strana-1)
#         #print(f"kreslim posledny troj{nova_strana}")

for i in range(-140,71,70):
    print(i)


    t.goto(x=h+1,y=i)
    new_dlzka = 0
    old_dlzka = 0
    #print(sirka)
    while sirka > new_dlzka:
        dl = random.randint(20,80)
        #print(f"increment to be extended:{dl}")
        new_dlzka += dl
        #print(f"kandidat dlzka napocitna:{new_dlzka,sirka}")
        #print(f"som vo while")
        if new_dlzka < sirka:
            #print(f"som v if")
            troj(dl)
            old_dlzka += dl
            #pozicia = t.xcor()
    else:
        nova_strana = sirka - old_dlzka   #dokreslim zvysny trojuholnik
        troj(nova_strana-1)
        #print(f"kreslim posledny troj{nova_strana}")


screen.mainloop()
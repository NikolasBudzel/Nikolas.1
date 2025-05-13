import tkinter as tk


root =tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def zmena(farba):
    label= tk.Label(root, image=farba).place(x=290, y=441)
    label.pack()
    label1 = tk.Label(root, image=farba).place(x=463, y=341)
    label2 = tk.Label(root, image=farba).place(x=463, y=141)
    label3 = tk.Label(root, image=farba).place(x=290, y=59)
    label4 = tk.Label(root, image=farba).place(x=117, y=159)
    label5 = tk.Label(root, image=farba).place(x=117, y=359)





salka_ruzova = tk.PhotoImage(file="salka4.png")
salka_fialova = tk.PhotoImage(file="salka3.png")
salka_modra = tk.PhotoImage(file="salka2.png")
salka_zelena = tk.PhotoImage(file="salka1.png")
salka_zlta = tk.PhotoImage(file="salka0.png")

tl_zlta = tk.PhotoImage(file="farba0.png")
tl_zelena = tk.PhotoImage(file="farba1.png")
tl_modra = tk.PhotoImage(file="farba2.png")
tl_fialova = tk.PhotoImage(file="farba3.png")
tl_ruzova = tk.PhotoImage(file="farba4.png")

button_zlta = tk.Button(root, image=tl_zlta, command=zmena(salka_zlta))
canvas.create_window(0,0,window=button_zlta)
button_zlta.image = tl_zlta
button_zelena = tk.Button(root, image=tl_zelena, command=zmena("salka1.png"))
canvas.create_window(0,35,window=button_zelena)
button_zelena.image = tl_zelena
button_modra = tk.Button(root, image=tl_modra, command=zmena("salka2.png"))
canvas.create_window(0,70,window=button_modra)
button_modra.image = tl_modra
button_fialova = tk.Button(root, image=tl_fialova, command=zmena("salka3.png"))
canvas.create_window(0,105,window=button_fialova)
button_fialova.image = tl_fialova
button_ruzova = tk.Button(root, image=tl_ruzova, command=zmena("farba4.png"))
canvas.create_window(0,140,window=button_ruzova)
button_ruzova.image = tl_ruzova

# tk.Label(root, image=).place(x=290, y=441)
# tk.Label(root, image=).place(x=463, y=341)
# tk.Label(root, image=).place(x=463, y=141)
# tk.Label(root, image=).place(x=290, y=59)
# tk.Label(root, image=).place(x=117, y=159)
# tk.Label(root, image=).place(x=117, y=359)


root.mainloop()
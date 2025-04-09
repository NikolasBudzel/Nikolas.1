import turtle
import random

turtle.penup()
turtle.goto(x=0,y=-380)
turtle.pendown()

def padajuci_troj(dlzka):

    nahodny_uhol = (random.randint(-20,20))
    turtle.setheading(nahodny_uhol)
    turtle.forward(dlzka/2)
    turtle.left(120)
    turtle.forward(dlzka)
    turtle.left(120)
    turtle.forward(dlzka)
    turtle.left(120)
    turtle.forward(dlzka/2)
    turtle.left(180)
    turtle.forward(dlzka/2)
    turtle.right(120)
    turtle.forward(dlzka)

for _ in range(3,7):
    padajuci_troj(random.randint(30,100))




turtle.done()
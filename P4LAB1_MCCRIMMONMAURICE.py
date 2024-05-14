#Maurice Mccrimmon
#3/26/2024
#P4LAB1
#Using loops to draw shapes

import turtle
win = turtle.Screen()
timmy = turtle.Turtle()

timmy.pensize(4)
timmy.pencolor("green")
timmy.shape("arrow")

for side in range(4):
    timmy.forward(75)
    timmy.right(90)

counter = 0
while counter < 3:
    timmy.forward(75)
    timmy.left(120)
    counter += 1

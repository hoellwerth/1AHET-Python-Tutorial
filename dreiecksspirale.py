from turtle import *

def drawRectangle(s):
    for n in range(3):
        forward(s)
        left(120)

    left(10)

shape('turtle')
speed(10)

color('white')
bgcolor('black')

for i in range(300, 0, -10):
    drawRectangle(i)

exitonclick()
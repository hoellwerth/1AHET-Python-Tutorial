from turtle import *

shape('turtle')
speed(10)

color('white')
bgcolor('black')

for i in range(300, 0, -10):
    for n in range(3):
        forward(i)
        left(120)

    left(10)

exitonclick()
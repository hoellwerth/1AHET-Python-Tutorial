import turtle

turtle.shape('turtle')
turtle.speed(10)

turtle.color('white')
turtle.bgcolor('black')

for i in range(300, 0, -10):
    for n in range(3):
        turtle.forward(i)
        turtle.left(120)

    turtle.left(10)

turtle.exitonclick()
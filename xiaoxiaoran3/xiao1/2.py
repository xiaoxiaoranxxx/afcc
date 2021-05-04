from turtle import *

setup(600, 400)
bgcolor("red")
fillcolor("yellow")
color('yellow')
speed(10)


def xiao(x1, x2, degree, y=50):
    begin_fill()
    up()
    goto(x1, x2)
    setheading(degree)
    down()
    for i in range(5):
        forward(y)
        right(144)
    end_fill()


xiao(-280, 100, 0, 150)
xiao(-100, 180, 305)
xiao(-50, 110, 30)
xiao(-40, 50, 5)
xiao(-88, 10, 300)

hideturtle()
done()

from turtle import *


def go_to(x, y):
    up()
    goto(x, y)
    down()


def big_circle(size):
    speed(10)
    for i in range(150):
        forward(size)
        right(0.3)


def small_circle(size):
    speed(10)
    for i in range(210):
        forward(size)
        right(0.786)


def line(size):
    speed(1)
    forward(51 * size)


def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    line(size)
    big_circle(size)
    small_circle(size)
    left(120)
    small_circle(size)
    big_circle(size)
    line(size)
    end_fill()


def arrow():
    pensize(10)
    setheading(0)
    go_to(-400, 0)
    left(15)
    forward(150)
    go_to(339, 178)
    forward(150)


def arrow_head():
    pensize(1)
    speed(5)
    color('red', 'red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()


def main():
    window = Screen()
    window.setup(width=1.0, height=1.0, startx=None, starty=None)
    pensize(2)
    color('red', 'pink')
    heart(200, 0, 1)
    setheading(0)
    heart(-80, -100, 1.5)
    arrow()
    arrow_head()
    go_to(400, -300)
    done()


main()

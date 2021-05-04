from turtle import *
# 移动点
def move(x, y):
    up()
    goto(x, y)
    down()
# 画大星星
def draw_big(size, x, y):
    move(x, y)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
# 画小星星
def draw_small(size, x, y):
    move(x, y)
    begin_fill()
    for i in range(5):
        forward(size)
        left(144)
    end_fill()
 
bgcolor("red")
color("yellow")
fillcolor("yellow")
 
draw_big(100, -280, 170)
 
draw_small(40, -130, 240)
draw_small(40, -100, 180)
draw_small(40, -100, 120)
draw_small(40, -130, 60)
 
done()
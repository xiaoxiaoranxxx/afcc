# coding=gbk

from turtle import *

up()
goto(-200, 200)
down()
begin_fill()
fillcolor("red")
pencolor("red")
for i in range(2):
    forward(280)
    right(90)
    forward(200)
    right(90)
end_fill()

def xiu(x1, x2, y1=20):
    up()
    goto(x1, x2)
    down()
    begin_fill()
    fillcolor("yellow")
    pencolor("yellow")
    for x in range(5):
        forward(y1)
        right(144)
    end_fill()

xiu(-170, 145, 50)
xiu(-100, 180)
xiu(-70, 160)
xiu(-70, 120)
xiu(-100,100)

fillcolor("black")
pencolor("black")
penup()
goto(-280, -180)
pendown()
write('祖国万岁!', font=('华文行楷', '88', 'bold'))
hideturtle() 
done()

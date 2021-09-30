

from turtle import *  #导入画图模块

up()  #抬笔

goto(-200, 200) #到画长方形的起点
down()  #落笔

begin_fill()  # 开启颜色填充
fillcolor("red")
pencolor("red")

for i in range(2):  # 画正方形
    forward(300)
    right(90)
    forward(200)
    right(90) 
end_fill() # 结束红色填充

def xiu(x1, x2, y1=20):  # 画五角星
    up()
    goto(x1, x2)
    if(x1!=-170):
        setheading(12)
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

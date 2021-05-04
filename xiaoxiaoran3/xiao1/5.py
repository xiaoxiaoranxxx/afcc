import turtle as tu

tu.hideturtle()     #隐藏海龟
tu.speed(10)
tu.title("Chinese National Flag.")   #显示海龟绘图窗口的标题栏文本

n = float(tu.textinput("N","Please enter the times you want."))       #国旗放大的倍数,textinput()函数用于返回用户输入的参数

#旗面
tu.penup()
tu.goto(-150*n,100*n)
tu.pendown()
tu.pencolor("red")
tu.begin_fill()
tu.fillcolor("red")
tu.fd(300*n)
tu.right(90)
tu.fd(200*n)
tu.right(90)
tu.fd(300*n)
tu.right(90)
tu.fd(200*n)
tu.end_fill()

#大星星
tu.penup()
tu.goto(-100*n,80*n)
tu.pendown()
tu.pencolor("yellow")
tu.begin_fill()
tu.fillcolor("yellow")
tu.setheading(-72)
for i in range(5):
    tu.fd(57.06*n)
    tu.right(144)
tu.end_fill()

#小星星1
tu.penup()
tu.goto(-60*n,70*n)
tu.pendown()
tu.pencolor("yellow")
tu.begin_fill()
tu.fillcolor("yellow")
tu.setheading(70)
for i in range(5):
    tu.fd(19.02*n)
    tu.right(144)
tu.end_fill()

# 小星星2
tu.penup()
tu.goto(-40*n,63*n)
tu.pendown()
tu.pencolor("yellow")
tu.begin_fill()
tu.fillcolor("yellow")
tu.setheading(10)
for i in range(5):
    tu.fd(19.02*n)
    tu.right(144)
tu.end_fill()

#小星星3
tu.penup()
tu.goto(-36*n,25*n)
tu.pendown()
tu.pencolor("yellow")
tu.begin_fill()
tu.fillcolor("yellow")
tu.setheading(70)
for i in range(5):
    tu.fd(19.02*n)
    tu.right(144)
tu.end_fill()

# 小星星4
tu.penup()
tu.goto(-60*n,20*n)
tu.pendown()
tu.pencolor("yellow")
tu.begin_fill()
tu.fillcolor("yellow")
tu.setheading(-20)
for i in range(5):
    tu.fd(19.02*n)
    tu.right(144)
tu.end_fill()

tu.done()
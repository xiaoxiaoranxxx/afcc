import turtle

# turtle.setup(800,800,0,0)
# turtle.color('red')
# for i in range(100):
#     turtle.forward(100)
#     turtle.right(99)
#     turtle.showturtle()
#     turtle.pensize(10)
#     if i % 2 == 0:
#         turtle.penup()
#     else:
#         turtle.pendown()

# turtle.penup()
# turtle.goto(-50, -50)
# turtle.pendown()
# turtle.write('xiao', font=('华文行楷', '88', 'bold'))
# turtle.hideturtle()

# turtle.penup() #画笔抬起  别名turtle.pu()
# turtle.pendown()#画笔降下 别名turtle.pd()
# turtle.pensize(宽度) #画笔宽度
#                   别名turtle.width(宽度)
# turtle.pencolor(color) #画笔颜色  color为字符串 或者 R G B 的值

# turtle.speed(speed)：设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
# turtle.fillcolor(colorstring) 绘制图形的填充颜色
# turtle.color(color1,color2)同时设置画笔颜色color1, 填充颜色color2

# turtle.fd(d)表示向海龟前方
# turtle.bk(d)表示向海龟后方
# turtle.circle(半径,弧度)表示海龟以左侧某一点为圆心的曲线方向


# turtle.setheading(angle)#改变行进方向
#             #别名turtle.seth()
# turtle.left(angle) #向左转
# turtle.right(angle) #向右转


# from time import sleep

# turtle.setup(650, 350, 200, 200)  # 设置屏幕位置
# turtle.penup()  # 抬起画笔
# turtle.fd(-250)  # 向后退250（此时不画）
# turtle.pendown()  # 画笔落下
# turtle.pensize(25)  # 画笔宽度为25
# turtle.pencolor("blue")  # 画笔颜色为蓝色
# turtle.seth(-40)  # 向右转40
# for i in range(4):
#     turtle.circle(40, 80)  # 圆心在左侧半径40 画的弧度为80度（向下弯）
#     turtle.circle(-40, 80)  # 圆心在右侧半径40 画的弧度为80度（向上弯）
# turtle.done()  # 结束绘画后不立即退出，需要手动关闭


# turtle.pencolor("purple")
# turtle.pencolor(0.63,0.13,0.94)


# 显示器和turtle窗体的左上角都是原点
# turtle.setup(width,height,startx,starty)设置窗体大小及位置，后面两个参数可选，非必需
# 空间坐标：绝对坐标：右方向x轴，上方向为y轴，正中心为原点，turtle.goto(x,y)让在任何位置的海龟到达指定的位置
# 海龟坐标：turtle.fd(d)海龟向前行多少像素
# turtle.bk(d)向海龟的反方向运行
# turtle.circle(r,angle)以海龟左边的某一点为圆心进行曲线运行
# 角度坐标：绝对角度：turtle.seth(angle)angle为绝对度数，表示改变海龟的运行方向
# 海龟角度：turtle.right(angle),turtle.left(angle)改变海龟的运行方向
# RGB体系：turtle.colormode(mode)mode=1.0则改用0和1表示，mode=255则改用255和0表示，默认为小数
# 库引用：import <库名>,from <库名> import *或者from <库名> import <函数名>,import <库名> as <库别名>
# 画笔控制函数：turtle.penup() 别名：turtle.pu()
# 抬起画笔，turtle.pendown()别名：turtle.pd()落下画笔，
# turtle.pensize(width)别名：turtle.width(width)设置画笔宽度，turtle.pencolor(color)
# 设置画笔颜色，color有三种方式，颜色字符串，或者RGB小数值，或者RGB元组值，例如：turtle.pencolor((0.63,0.13,0.94))
# 运动控制函数:turtle.circle(r,angle),r（海龟左方向）表示半径，angle表示绘制的角度，默认是360度
# 方向控制函数：turtle.seth(angle)改变海龟的行进方向，顺时针转向


turtle.done()

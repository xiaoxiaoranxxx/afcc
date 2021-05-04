from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
speed(0)
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    #left(91)
    left(59)
done()
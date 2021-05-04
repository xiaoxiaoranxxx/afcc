import turtle as t

import time

#太阳花
t.color("red", "yellow")

t.speed(0)

t.begin_fill()

for _ in range(50):
    t.forward(200)
    t.left(170)
    t.end_fill()
    time.sleep(0.1)
t.done()
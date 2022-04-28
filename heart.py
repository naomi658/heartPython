import turtle as t
import math as m

t.color("red")
t.begin_fill()
t.up()
dot = 100
size = 15

for i in range(0, dot):
    h = m.pi*i/(dot/2)
    x = size*16*m.sin(h)** 3
    y = size*13*m.cos(h) - size*5*m.cos(2*h) - size*2*m.cos(3*h) - size*m.cos(4*h)
    t.goto(x, y)
    t.down()

t.end_fill()

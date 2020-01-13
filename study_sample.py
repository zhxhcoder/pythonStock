from sys import argv
from math import sin, pi
import turtle

n = int(550)
d = float(100)
t = turtle.Pen()
t.pensize(2)
for _ in range(n):
    t.forward(d * sin(pi / n))
    t.left(360 / n)
t.hideturtle()
turtle.exitonclick()

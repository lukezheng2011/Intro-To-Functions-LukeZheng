import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(123)

length=5
def star(length):
    for i in range(5):
        t.forward(length)
        t.right(144)

for i in range(60):
    
    star(length)
    length+=5
    t.right(5)









































turtle.done()


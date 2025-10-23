import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(123)

length=5
def star(length):
    for i in range(5):
        t.forward(length)
        t.right(44)

for i in range(202):
    
    star(length)
    length+=5
    t.left(5)









































turtle.done()


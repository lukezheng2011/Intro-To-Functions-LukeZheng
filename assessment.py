import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(123)

length=5

def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

for i in range(60):
    
    square(length)
    length+=5
    t.left(5)





























turtle.done()
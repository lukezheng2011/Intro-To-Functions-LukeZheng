import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

t.forward(200)

def square(x):  
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(55)

def triangleone(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
triangleone(126)

t.right(90)

def triangleright(x):
    t.forward(x)


turtle.done()

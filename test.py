import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(111)



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

#def triangleright():
 #   t.forward(50)
  #  t.right(90)
   # t.forward(120)
    #t.right(135)
    #t.forward(130)
#triangleright()

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()



def rect(x,y):
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
rect(100,125)


t.left(45)
t.forward(200)


def lasttri(x):
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
lasttri(90)

turtle.done()
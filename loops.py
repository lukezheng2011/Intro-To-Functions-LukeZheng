import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(123)

def square():
  for i in range(4):
    t.forward(100)
    t.left(90)
  square()
 
for i in range(80):
  square()
  t.right(5)


















turtle.done()
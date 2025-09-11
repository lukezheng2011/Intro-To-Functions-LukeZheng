import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(500)

length=5
def linea(length):
    for i in range(1):
        t.forward(length)
        t.right(180)
        t.forward(length)
        t.right(180)


    

for i in range(120):
    
    linea(length)
    length+=3
    t.left(6)



#seashell looking thingy





































turtle.done()


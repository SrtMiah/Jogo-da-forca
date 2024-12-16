import math
from turtle import *
import random

def hearta (k):
    return 16*math.sin(k)**3

def heartb (k):
    return 13*math.cos(k)-5*\
       math.cos(2*k)-2*\
       math.cos(3*k)-\
       math.cos(4*k)

def draw_heart():
    penup()
    goto(0, -200)
    pendown()
    begin_fill()
    for i in range (700):
       k = i / 100
       goto(hearta(i)*20, heartb(i)*20)
    end_fill()
    
def draw_firewoerks(x, y):
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for _ in range(20):
        penup()
        goto(x,y)
        pendown()
        color(random.choice(colors))
        setheading(random.randint(0, 360))
        for _ in range(36):
            forward(random.randint(50, 100))
            backward(random.randint(50, 100))
            left(10)

speed(0)
bgcolor("black")
color("#f73487")

draw_heart()

draw_firewoerks(0, 0)

hideturtle()
done()
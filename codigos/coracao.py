from turtle import *

setup(600, 600)
bgcolor("white")

color("red")
begin_fill()
pensize(3)
penup()
goto(0, -100)
pendown()

left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(0, -100)
pendown()
color("black")
left(140)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)

hideturtle()
done()
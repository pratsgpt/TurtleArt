import turtle

screen = turtle.Screen()
screen.bgcolor("white")

prats = turtle.Turtle()
"""
.shape("turtle") - to change cursor shape to turtle
.xcor(), .ycor() - x and y coordinates
 turtle.screensize() - to check current screensize
.forward(100)
.right(90)
.left(60)
.backward(100)
.color('red')
.circle(10)
.penup()
.pendown()
.reset()
.goto(35, 80)
.hideturtle()
"""
# printing a red square
"""prats.begin_fill()
prats.color('red')
for i in range(4):
    prats.forward(50)
    prats.left(90)
prats.end_fill()"""

#first geometric pattern with squares
"""for n in range(6):
    for i in range(4):
        prats.forward(50)
        prats.left(90)
    prats.right(60)"""
#prats.hideturtle() -- not working need to debug

#draw a hexagon pattern with colors
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']
#make 36 hexagons each 10 degrees apart
for n in range(36):
    #make hexagon
    for i in range(6):
        prats.color(colors[i])
        prats.forward(100)
        prats.left(60)
    prats.right(10)
turtle.done()

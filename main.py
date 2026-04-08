from turtle import *

screen = Screen()
screen.bgcolor("teal")
screen.title("Write your name")
screen.setup(width = 1500, height = 400)

# Movement - Forward, Backward, Right, Left

yertle = Turtle()
yertle.color("white")
yertle.shape() # circle, square, triangle, or turtle
yertle.speed(2)

# for j in range(4):
#     for i in range(5):
#         yertle.forward(10)
#         yertle.penup()
#         yertle.forward(10)
#         yertle.pendown()
#     yertle.left(90)
# while True:
#     '''
#     East is 0, 
#     North is 90, 
#     West is 180, 
#     South is 270 or -90
#     '''
#     angle = float(input("Enter a degree"))
#     yertle.setheading(angle)

# Movement - coordinates
yertle.pensize(20)
yertle.pencolor("red")
yertle.penup()
yertle.goto(-400, -150)
yertle.pendown()
yertle.sety(75)
yertle.left(45)
yertle.forward(100)
yertle.penup()
yertle.left(90)
yertle.setx(-400)
yertle.sety(75)
yertle.pendown()
yertle.forward(100)
yertle.penup()
yertle.color("white")
yertle.setx(-350)
yertle.sety(0)
yertle.setheading(270)
yertle.pendown()
yertle.circle(150)
yertle.color("black")
yertle.penup()
yertle.setheading(0)
yertle.forward(335)
yertle.pendown()
yertle.sety(150)
yertle.right(90)
yertle.penup()
yertle.forward(150)
yertle.pendown()
yertle.forward(100)
yertle.circle(40, 180)
yertle.forward(250)
yertle.color("brown")
yertle.right(90)
yertle.penup()
yertle.forward(110)
yertle.pendown()
yertle.circle(-75, -180)
yertle.circle(75, -180)
yertle.penup()
yertle.forward(125)
yertle.pendown()
yertle.color("beige")
yertle.left(90)
yertle.forward(300)
yertle.right(180)
yertle.forward(300)
yertle.penup()
yertle.left(90)
yertle.pendown()
yertle.forward(100)
yertle.left(90)
yertle.penup()
yertle.forward(150)
yertle.left(90)
yertle.forward(100)
yertle.pendown()
yertle.backward(100)
yertle.penup()
yertle.setheading(90)
yertle.forward(150)
yertle.left(90)
yertle.forward(100)
yertle.pendown()
yertle.backward(100)
yertle.color("yellow")
yertle.penup()
yertle.backward(50)
yertle.pendown()
yertle.backward(100)
yertle.forward(100)
yertle.left(90)
yertle.forward(300)
yertle.backward(150)
yertle.setheading(0)
yertle.forward(100)






screen.exitonclick()
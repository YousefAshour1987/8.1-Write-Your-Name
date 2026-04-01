from turtle import *

screen = Screen()
screen.bgcolor("teal")
screen.title("Write your name")
screen.setup(width = 1000, height = 400)

# Movement - Forward, Backward, Right, Left

yertle = Turtle()
yertle.color("white")
yertle.shape() # circle, square, triangle, or turtle
yertle.speed(1)

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
# yertle.hideturtle()
# yertle.penup()
# yertle.goto(-100, -100)
# yertle.pendown()
# yertle.goto(-100, 100)
# yertle.setx(100)
# yertle.sety(-100)
# yertle.goto(-100, -100)

yertle.circle(100, 80)
yertle.forward(5)
yertle.left(2)
yertle.forward(1)
    







screen.exitonclick()
import turtle as t
from turtle import Screen
import random

color_list = [(246, 245, 243), (235, 240, 246), (246, 240, 243), (241, 246, 243), (131, 165, 205),
              (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46)]

starting_position_x = -200
starting_position_y = -200

change_position = 50
tim = t.Turtle()
tim.penup()
tim.goto(starting_position_x, starting_position_y)
tim.pencolor("")
my_screen = Screen()
my_screen.setup(300, 300)
my_screen.colormode(255)

def move_forward():
    for i in range(10):
        tim.hideturtle()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(40)
        tim.pendown()
        tim.forward(20)

for i in range(10):
    move_forward()
    starting_position_y += change_position
    tim.goto(starting_position_x, starting_position_y)
    tim.pendown()

my_screen.exitonclick()
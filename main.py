from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput("Make your bet", "Which turtle win the race? Enter a color: ")
print(user_bet)

y = 200
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    y -= 55
    tim.goto(-230, y)






screen.exitonclick()

from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput("Make your bet", "Which turtle win the race? Enter a color: ")
print(user_bet)
y = 200

turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y -= 55
    new_turtle.goto(-230, y)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is winner!")

        move = random.randint(0, 10)
        turtle.forward(move)

screen.exitonclick()

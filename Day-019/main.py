from turtle import Turtle, Screen
from random import randint
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


all_turtles = []
y = -125
for t in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner_t = turtle.pencolor()
            if winner_t == user_bet:
                print(
                    f"You've won! The {winner_t} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winner_t} turtle is the winner!")

        randmove = randint(0, 10)
        turtle.forward(randmove)

screen.exitonclick()

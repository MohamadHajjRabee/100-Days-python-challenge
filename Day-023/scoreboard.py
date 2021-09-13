from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard:
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color("black")
        self.t.goto(-270, 270)
        self.level = 1
        self.print_level()

    def print_level(self):
        self.t.clear()
        self.t.goto(-270, 270)
        self.t.write(f"Level :{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.t.goto(0, 0)
        self.t.write("GAME OVER.", align="center", font=FONT)

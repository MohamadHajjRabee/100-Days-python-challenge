from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False,
                   align="center", font=("Courier", 15, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center",
                   font=("Courier", 15, "normal"))

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.08

    def move(self):

        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        if self.xcor() > 400 or self.xcor() < -400:
            self.goto(0, 0)
            self.x_move *= -1
            self.move_speed = 0.08

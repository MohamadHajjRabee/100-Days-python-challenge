from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []


class CarManager:
    def __init__(self):
        self.create_car()
        self.move_speed = 10

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        rand_color = random.choice(COLORS)
        car.color(rand_color)
        rand_y = random.randint(-250, 250)
        car.goto(300, rand_y)
        CARS.append(car)

    def move_car(self):
        for car in CARS:
            car.goto(car.xcor() - self.move_speed, car.ycor())

        self.rand_num = random.randint(0, 4)
        if self.rand_num == 2:
            self.create_car()

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def car(self):
        all_cars = CARS
        return all_cars

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")
car_manager = CarManager()

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:

    # Detect if player hit the car
    for car in car_manager.car():
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player finished the line
    if player.ycor() == player.finish_line:
        car_manager.increase_speed()
        player.refresh_player()
        scoreboard.increase_level()
        scoreboard.print_level()

    car_manager.move_car()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()

import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.listen()

screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
game_is_on = True

screen.onkeypress(fun=player.move_up, key="w")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.car_move()

    if player.ycor() > 260:
        scoreboard.scoreboard_update()
        player.reset_position()
        car_manager.update_speed()

    for car in car_manager.car_list:
        if player.distance(car) < 27:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
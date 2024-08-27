import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.car_list = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_cor = random.randint(-250, 250)
            new_car.goto(300, random_y_cor)
            self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def update_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT



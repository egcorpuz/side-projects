from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ODDS_INCREMENT = 1


class CarManager:

    def __init__(self) -> None:
        self.car_list = []
        self.carspeed = MOVE_INCREMENT
        # self.generate_car()

    def generate_car(self):
        chance_car = random.randint(ODDS_INCREMENT, 6)
        if chance_car == ODDS_INCREMENT:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)
        
    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE, ODDS_INCREMENT
        STARTING_MOVE_DISTANCE += self.carspeed
        if ODDS_INCREMENT == 6:
            ODDS_INCREMENT = 6
        else:
            ODDS_INCREMENT += 1
    
    def pop_cars(self, car):
        car.hideturtle()
        self.car_list.remove(car)
        del car

    @staticmethod
    def reset_speed():
        global STARTING_MOVE_DISTANCE, ODDS_INCREMENT
        STARTING_MOVE_DISTANCE = 5
        ODDS_INCREMENT = 1

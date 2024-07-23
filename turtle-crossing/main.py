import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
cars.generate_car()

player1 = Player()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(player1.move_up, "Up")
    screen.onkeypress(player1.move_down, "Down")
    cars.move_cars()
    
    # Generate new cars on the screen every 6 iteration
    cars.generate_car()
    
    # Pop cars when they reach the lelftmost other sideof the screen
    # Detect collision with any car
    for car in cars.car_list:
        if car.xcor() < -290:
            cars.pop_cars(car)
        if player1.distance(car) < 20 and player1.distance(car) > car.ycor() - 30:
            scoreboard.game_over()
            game_is_on = False
    
    # Detect if turtle has crossed to the other side
    if player1.ycor() > 280:
        scoreboard.p1_point()
        scoreboard.update_scoreboard()
        cars.increase_speed()
        player1.reset_position()

screen.exitonclick()

# TODO: Implement in PyGame
# TODO: ✅ pop cars when they reach the other side
# TODO: ✅ increase car generation odds as we increase speed
# TODO: add hard mode where you can't move backwards
# TODO: generate life for the player, for normal  mode
# TODO: For normal mode, lives get deducted, player resets to position
# TODO: FOr normal mode, Player resets to position, same level
# TODO: For normal mode, if lives is 0, reset  to level 1

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

DELAY_TIME = 0.1
WALLS = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game: Classic")
screen.tracer(0)
# this turns off the animation until update is called

snake = Snake()
food = Food()
food.refresh()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score_board = ScoreBoard()
score_board.print_score()

is_game_on = True
while is_game_on:
    screen.update()
    # moving all the blocks before updating/refreshing the screen
    time.sleep(DELAY_TIME)
    # 1-second delay to watch what happens
    # consequently, the delay time controls the speed of the snake
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_update()

    # Detect collision with wall.
    if snake.head.xcor() > WALLS or snake.head.xcor() < -1*WALLS or snake.head.ycor() > WALLS or snake.head.ycor() < -1*WALLS:
        score_board.reset()
        snake.reset()
    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # This slice allows as to not consider the head segment colliding with itself
        if snake.head.distance(segment) < 10:
            score_board.reset()

screen.exitonclick()

# TODO: Implement using PyGame
# TODO: DID Set and remember new high scores (use JSON?)
# TODO: Add easy mode (colliding with body part is okay)
# TODO: Add fun mode (colliding with wall makes the snake to turn around)
# TODO: Change snake color, change food object shape and color
# TODO: Make collision with tail more efficient (not using loops but cache)

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_XPOS = 350
WALLS = 280
SIDE_WALLS = 380
PADDLE_WALLS = 320
BALL_TO_PADDLE = 50
# PADDLE_YPOS = 250

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong: Classic")

screen.tracer(0)
# -1 makes the position to the left of the screen
player1 = Paddle(-1 * PADDLE_XPOS, 0)
player2 = Paddle(PADDLE_XPOS, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

is_game_on = True

while is_game_on:
    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(ball.ballspeed)
    # the delay time also adjusts the speed of the ball
    ball.move()

    screen.onkeypress(player1.go_up, "w")
    screen.onkeypress(player1.go_down, "s")
    screen.onkeypress(player2.go_up, "Up")
    screen.onkeypress(player2.go_down, "Down")

    # Detect collision with top or bottom wall
    if ball.ycor() > WALLS or ball.ycor() < -1 * WALLS:
        ball.bounce_y()

    # Detect contact with paddles
    if ball.distance(player2) < BALL_TO_PADDLE and ball.xcor() > PADDLE_WALLS or ball.distance(
            player1) < BALL_TO_PADDLE and ball.xcor() < -1 * PADDLE_WALLS:
        ball.bounce_x()
    
    # right player misses
    if ball.xcor() > SIDE_WALLS:
        scoreboard.p1_point()
        ball.reset_position()

    # left player misses
    if ball.xcor() < -1*SIDE_WALLS:
        scoreboard.p2_point()
        ball.reset_position()

screen.exitonclick()

# TODO: Implement using PyGame
# TODO: add fun modes where paddles get closer to each other
# TODO: add modes where there are top and bottom players
# TODO: From suggestion above, make the ball pass through instead of bouncing off the top and bottom walls

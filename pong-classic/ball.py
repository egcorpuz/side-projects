from turtle import Turtle

MOVE_DISTANCE = 10
WALLS = 300
x_neg, y_neg = 1, 1


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.ballspeed = 0.1

    def move(self):
        global x_neg, y_neg
        new_x = self.xcor() + x_neg*MOVE_DISTANCE
        new_y = self.ycor() + y_neg*MOVE_DISTANCE
        self.goto(new_x, new_y)

    @staticmethod
    def bounce_y():
        global y_neg
        y_neg *= -1

    def bounce_x(self):
        global x_neg
        x_neg *= -1
        self.ballspeed *= 0.5
    
    def reset_position(self):
        global x_neg
        x_neg *= -1
        self.goto(0, 0)
        self.ballspeed = 0.1

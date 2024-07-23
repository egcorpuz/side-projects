from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.gamelevel = 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Score: {self.p1_score}", align="left", font=FONT)
        self.goto(250, 250)
        self.write(f"Level: {self.gamelevel}", align="right", font=FONT)

    def p1_point(self):
        self.p1_score += 1
        self.gamelevel += 1

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

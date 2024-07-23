from turtle import Turtle

with open("data.txt") as data:
    HIGHSCORE = int(data.read())

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
Y_COR = 265


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=Y_COR)
        self.score = 0
        self.high_score = HIGHSCORE

    def score_update(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.print_score()

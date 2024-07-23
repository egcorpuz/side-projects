from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self) -> None:
        self.segments = []
        # initialize your snake's attributes here
        # you can call a function here from below
        # code still reads top-down
        self.create_snake()
        self.head = self.segments[0]
        # since code reads top-down, make sure this line of code
        # is under the function call

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        current_heading = self.head.heading()
        if current_heading == DOWN:
            return
        self.head.setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading == UP:
            return
        self.head.setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading == RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading == LEFT:
            return
        self.head.setheading(RIGHT)

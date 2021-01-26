from turtle import Turtle

START_POSITION = -280
END_POSITION = 280
MOVE_SPEED = 10


class Player(Turtle):
    # Create a Player-Turtle
    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(START_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_SPEED)
from turtle import Turtle

START_POSITION = -280
END_POSITION = 280
MOVE_SPEED = 10


class Player(Turtle):
    # Create a Player-Turtle
    def __init__(self):
        super().__init__()
        self.reset_player()

    def reset_player(self):
        self.penup()
        self.sety(START_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.color('pink')

    def move(self):
        self.forward(MOVE_SPEED)
        # print(f"xcor: {round(self.xcor())} ycor: {self.ycor()}")

    def is_finish(self):
        return self.ycor() > END_POSITION

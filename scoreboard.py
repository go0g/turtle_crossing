from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align='left', font=("Arial", 16, "normal"))

    def add_level(self):
        self.level += 1
        self.write_score()


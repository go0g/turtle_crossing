from turtle import Screen
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

game_run = True

while game_run:
    screen.update()
    time.sleep(0.1)
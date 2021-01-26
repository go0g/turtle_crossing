from turtle import Screen
import time

from player import Player

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, 'w')

game_run = True

while game_run:
    screen.update()
    time.sleep(0.1)
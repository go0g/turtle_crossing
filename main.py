from turtle import Screen
import time

from player import Player
from scoreboard import Scoreboard, GameOverScreen
from traffic_control import TrafficControl

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
traffic = TrafficControl()

screen.listen()
screen.onkey(player.move, 'w')
screen.onkey(screen.bye, 'x')

game_run = True

while game_run:
    screen.update()
    traffic.move()
    if traffic.collision_control(player):
        game_run = False
    if player.is_finish():
        player.reset_player()
        scoreboard.add_level()
    time.sleep(0.1)

while True:
    screen.update()
    game_over = GameOverScreen()

from turtle import Screen

from block_manager import BlockManager
from ball_manager import BallManager
from platform_manager import PlatformManager


screen = Screen()
screen.setup(width=715, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
block_manager = BlockManager()
ball_manager = BallManager()
platform_manager = PlatformManager()

block_manager.create_blocks()
screen.update()

while(game_is_on):
    ball_manager.move_ball()
    screen.update()

screen.exitonclick()

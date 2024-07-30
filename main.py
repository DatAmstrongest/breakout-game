from turtle import Screen

from block_manager import BlockManager
from ball_manager import BallManager


screen = Screen()
screen.setup(width=715, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
block_manager = BlockManager()
ball_manager = BallManager()

block_manager.create_blocks()
screen.update()

screen.exitonclick()

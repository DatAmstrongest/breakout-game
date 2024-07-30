from turtle import Screen

from block_manager import BlockManager


screen = Screen()
screen.setup(width=715, height=600)
screen.tracer(0)

game_is_on = True
block_manager = BlockManager()
block_manager.create_blocks()
screen.update()

while (game_is_on):
    print("ameno")
screen.exitonclick()

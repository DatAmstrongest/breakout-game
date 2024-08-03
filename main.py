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
platform_manager = PlatformManager(screen=screen)

block_manager.create_blocks()
screen.update()

while(game_is_on):
    ball_manager.move_ball()
    
    block_index = ball_manager.is_hit_to_block(block_manager.blocks)
    if block_index >= 0:
        block_manager.delete_block(block_index=block_index)
        ball_manager.change_direction(is_block_hit=True, platform=platform_manager.platform)
    else:
        ball_manager.change_direction(is_block_hit=False, platform=platform_manager.platform)
    screen.update()

screen.exitonclick()

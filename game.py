from turtle import Screen

from block_manager import BlockManager
from ball_manager import BallManager
from platform_manager import PlatformManager


class Game():
    def __init__(self):
        self.game_is_on = True
        self.screen = self.set_screen()
        self.ball_manager = BallManager()
        self.block_manager = BlockManager()
        self.platform_manager = PlatformManager(screen=self.screen)


    def set_screen(self):
        screen = Screen()
        screen.setup(width=715, height=600)
        screen.bgcolor("black")
        screen.tracer(0)
        return screen


    def start_game(self):
        self.block_manager.create_blocks()
        self.ball_manager.create_ball()
        self.screen.update()
        while(self.game_is_on):
            self.ball_manager.move_ball()
            block_index = self.ball_manager.is_hit_to_block(self.block_manager.blocks)
            if self.ball_manager.is_hit_vertical_lower_border():
                self.restart_game()
            if block_index >= 0:
                self.block_manager.delete_block(block_index=block_index)
                self.ball_manager.change_direction(is_block_hit=True, platform=self.platform_manager.platform)
            else:
                self.ball_manager.change_direction(is_block_hit=False, platform=self.platform_manager.platform)
            self.screen.update()
        self.screen.exitonclick()


    def restart_game(self):
        self.block_manager.delete_all_blocks()
        self.ball_manager.delete_ball()
        self.start_game()


from turtle import Screen, Turtle

from block_manager import BlockManager
from ball_manager import BallManager
from platform_manager import PlatformManager

LIVES = 3
FONT = ("comic sans", 36, "bold")


class Game():
    def __init__(self):
        self.game_is_on = True
        self.screen = self.set_screen()
        self.ball_manager = BallManager()
        self.block_manager = BlockManager()
        self.platform_manager = PlatformManager(screen=self.screen)
        self.lives = LIVES
        self.set_lives_counter()

    def set_screen(self):
        screen = Screen()
        screen.setup(width=715, height=600)
        screen.bgcolor("black")
        screen.tracer(0)
        return screen

    def set_lives_counter(self):
        lives_label = Turtle()
        lives_label.hideturtle()
        lives_label.penup()
        lives_label.goto(300, 250)
        lives_label.color("red")
        lives_label.write(self.lives, font=FONT)
        self.lives_label = lives_label

    def start_game(self):
        self.block_manager.create_blocks()
        self.ball_manager.create_ball()
        self.screen.update()
        while(self.game_is_on):
            self.ball_manager.move_ball()
            block_index = self.ball_manager.is_hit_to_block(self.block_manager.blocks)
            if self.ball_manager.is_hit_vertical_lower_border():
                self.lower_health()
                if self.lives == 0:
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
        self.lives = 3
        self.set_health()
        self.start_game()
    
    def lower_health(self):
        self.ball_manager.delete_ball()
        self.ball_manager.create_ball()
        self.lives -= 1
        self.set_health()
        
    def set_health(self):
        self.lives_label.clear()
        self.lives_label.write(self.lives, font=FONT)


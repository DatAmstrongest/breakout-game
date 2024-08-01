from turtle import Turtle

CURRENT_X_DIRECTION = 1
CURRENT_Y_DIRECTION = 1
SPEED = 3
HIT_DISTANCE = 40
X_BOUNDARY = 357
Y_BOUNDARY = 300

class BallManager():
    def __init__(self):
        self.create_ball()

    def create_ball(self):
        self.ball = Turtle()
        self.ball.color("grey")
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.goto(0,-225)

    def move_ball(self):
        self.ball.goto(self.ball.xcor()+SPEED*CURRENT_X_DIRECTION, self.ball.ycor()+SPEED*CURRENT_Y_DIRECTION)
    

    def is_hit_to_block(self, blocks):
        for i in range(len(blocks)):
            block = blocks[i]
            if self.ball.distance(block) <= HIT_DISTANCE:
                return i
        return -1
    

    def is_hit_horizontal_border(self):
        return self.ball.xcor() >= X_BOUNDARY or self.ball.xcor() <= X_BOUNDARY*-1 
    

    def is_hit_vertical_border(self):
        return self.ball.ycor() >= Y_BOUNDARY or self.ball.ycor() <= -1*Y_BOUNDARY
    

    def change_direction(self, is_block_hit):
        global CURRENT_X_DIRECTION
        global CURRENT_Y_DIRECTION

        if is_block_hit:
            CURRENT_Y_DIRECTION = CURRENT_Y_DIRECTION*(-1)
        elif self.is_hit_horizontal_border():
            CURRENT_X_DIRECTION = CURRENT_X_DIRECTION*(-1)
        elif self.is_hit_vertical_border():
            CURRENT_Y_DIRECTION = CURRENT_Y_DIRECTION*(-1)



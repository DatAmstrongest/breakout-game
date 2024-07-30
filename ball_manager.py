from turtle import Turtle

CURRENT_X_DIRECTION = 1
CURRENT_Y_DIRECTION = 1
SPEED = 1

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


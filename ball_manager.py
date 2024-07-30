from turtle import Turtle

class BallManager():
    def __init__(self):
        self.create_ball()

    def create_ball(self):
        self.ball = Turtle()
        self.ball.color("grey")
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.goto(0,-225)


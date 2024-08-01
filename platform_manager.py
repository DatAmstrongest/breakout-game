from turtle import Turtle
class PlatformManager():
    def __init__(self):
        self.create_platform()
    
    def create_platform(self):
        self.platform = Turtle()
        self.platform.color("blue")
        self.platform.shape("square")
        self.platform.shapesize(stretch_wid=1, stretch_len=5)
        self.platform.penup()
        self.platform.goto(0, -250)


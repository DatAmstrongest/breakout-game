from turtle import Turtle

SPEED = 20
class PlatformManager():
    def __init__(self, screen):
        self.create_platform(screen)
    
    def create_platform(self, screen):
        self.platform = Turtle()
        self.screen = screen
        self.platform.color("blue")
        self.platform.shape("square")
        self.platform.shapesize(stretch_wid=1, stretch_len=5)
        self.platform.penup()
        self.platform.goto(0, -250)
        self.set_keybindings()
        self.screen.listen()

    def set_keybindings(self):
        self.screen.onkey(self.left_key, "Left")
        self.screen.onkey(self.right_key, "Right")
    
    def left_key(self):
        self.platform.setheading(180)
        self.platform.forward(SPEED)
    def right_key(self):
        self.platform.setheading(0)
        self.platform.forward(SPEED)



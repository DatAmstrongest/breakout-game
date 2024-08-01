from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]
NUM_OF_ROWS = 5
NUM_OF_COLS = 10

class BlockManager():
    def __init__(self):
        self.blocks = []

    def create_blocks(self):
        for r in range(NUM_OF_ROWS):
            color = COLORS[r]
            for c in range(NUM_OF_COLS):
                block = Turtle()
                block.color(color)
                block.shape("square")
                block.shapesize(stretch_wid=2, stretch_len=3)
                block.penup()
                block.goto(-320+70*c, 25+50*r)
                self.blocks.append(block)

    def delete_block(self, block_index):
        block = self.blocks.pop(block_index)
        block.clear()
        block.ht()
        del block

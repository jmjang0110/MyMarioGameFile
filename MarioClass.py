from pico2d import *
from enum import Enum
import random

class Direction(Enum):
    STOP = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    JUMP = 5
    Circle = 6


class Mario:
    def __init__(self):
        self.image_right = load_image('mario_right.png')
        self.image_left = load_image('mario_left.png')
        self.image_Width = 100
        self.image_Height = 98

        self.direction = Direction.RIGHT
        self.x, self.y = random.randint(50,400), 90
        self.frame = 0

    def update(self):
        self.x += 5
        if self.x >= 700:
            self.x = 700

        self.frame = (self.frame + 1) % 3


    def draw(self):
        if self.direction == Direction.RIGHT:
            self.image_right.clip_draw(self.frame * self.image_Width,self.image_Height, 100,100, self.x, self.y)

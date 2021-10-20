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
        self.image_Height = 100

        self.Character_Width = 100
        self.Character_Height = 98

        self.direction = Direction.RIGHT
        self.x, self.y = random.randint(50,400), 90
        self.dst = 1
        self.frame = 0

    def update(self):
        self.x += (5 * self.dst)
        if self.x >= 800:
            self.x = 800
        elif self.x <= 0:
            self.x = 0


        self.frame = (self.frame + 1) % 2

    #   캐릭터의 방향을 바꿉니다.
    def ChangeDirection(self, NewDirection):
        self.direction = NewDirection
        self.UpdateDst()


    # 방향에 따른 좌표 이동 방향을 바꿉니다.
    def UpdateDst(self):
        if self.direction == Direction.RIGHT:
            self.dst = 1
        elif self.direction == Direction.LEFT:
            self.dst = -1



    def draw(self):
        if self.direction == Direction.RIGHT:
            self.image_right.clip_draw(300 + self.frame * self.image_Width, self.image_Height * 3,
                                       self.Character_Width, self.Character_Height, self.x, self.y)
        elif self.direction == Direction.LEFT:
            self.image_left.clip_draw(200 + self.frame * self.image_Width, self.image_Height,
                                      self.Character_Width, self.Character_Height, self.x, self.y)
        elif self.direction == Direction.STOP:
            self.image_right.clip_draw(self.frame * self.image_Width,self.image_Height,
                                       self.Character_Width, self.Character_Height, self.x, self.y)
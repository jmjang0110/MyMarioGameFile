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
        self.image_WIDTH = 100
        self.image_HEIGHT = 98

        self.direction = Direction.RIGHT
        self.x, self.y = random.randint(50,400), 90
        self.dst = 1
        self.frame, self.frame_dst = 0, 1

        # 점프를 위한 변수
        self.isJump = False
        self.jumpX = 10.0
        self.jumpY = 90.0
        self.diameter = 10.0

        self.jumpTime = 0.0
        self.jumpHeight = 0.0
        self.jumpPower = 40.0

        self.Velocity = 0.0
        self.Gravity = 400.0
        self.posY = 0.0


    def Jump(self):
        self.jumpHeight = (self.jumpTime * self.jumpTime - self.jumpPower * self.jumpTime) / 4.0
        self.jumpTime += 4.5
        # print(self.jumpHeight)

        self.y = self.posY + self.jumpHeight * -1

        print(self.jumpTime , '  ',  self.jumpPower)

        if self.y < 90:
            self.jumpTime = 0
            self.jumpHeight = 0
            self.isJump = False
            self.y = 90

        # if self.jumpTime > self.jumpPower:
        #     self.jumpTime = 0
        #     self.jumpHeight = 0
        #     self.isJump = False


    def Jump2(self):

        self.y = self.y + self.jumpHeight * 1

        if self.Velocity >= 300.0:
            self.Velocity = 300.0
            self.isJump = False
            self.jumpHeight = 0

        self.jumpHeight += self.Velocity * 0.0004
        self.Velocity += self.Gravity * 0.0004

    def update(self):
        if self.isJump == True:
             self.Jump()

        self.x +=( 5  *self.dst)
        if self.x >= 800:
            self.x = 800
        elif self.x <= 0:
            self.x = 0

        self.frame = (self.frame + 1) % 3

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
        # self.image_Mario2.
        if self.direction == Direction.RIGHT:
            self.image_right.clip_draw(self.frame * self.image_WIDTH, self.image_HEIGHT,
                                        self.image_WIDTH, self.image_HEIGHT, self.x , self.y, 100, 98)
        if self.direction == Direction.LEFT:
            self.image_left.clip_draw(200 + self.frame * self.image_WIDTH, self.image_HEIGHT,
                                       self.image_WIDTH, self.image_HEIGHT, self.x, self.y, 100, 98)
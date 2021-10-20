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

WINDOW_SIZE_WIDTH = 800
WINDOW_SIZE_HEIGHT = 600


class Mario:
    def __init__(self):
        self.BackGround_forTest = load_image('Mario_BackGround_Test.png')
        self.image_right = load_image('mario_right.png')
        self.image_left = load_image('mario_left.png')
        self.image_WIDTH = 100
        self.image_HEIGHT = 98

        self.direction = Direction.RIGHT
        self.jumpdirection = Direction.UP

        self.x, self.y = random.randint(50,400), 120
        self.dst = 1
        self.frame, self.frame_dst = 0, 1

        # 점프를 위한 변수
        self.isJump = False
        self.jumpX = 10.0
        self.jumpY = 120.0
        self.diameter = 10.0

        self.jumpTime = 0.0
        self.jumpHeight = 0.0
        self.jumpPower = 50.0  # 이 값을 높이면 더 높이 점프 할 수 있습니다.
        self.jumpSpeed = 4.0   # 이 값을 높이면 점프하는 속도가 빨라집니다..
        self.posY = 0.0        # 마리오 점프 시작 위치


    def Jump(self):
        self.jumpHeight = (self.jumpTime * self.jumpTime - self.jumpPower * self.jumpTime) / 4.0
        self.jumpTime += self.jumpSpeed
        # 마리오 : 점프에 따른 y값 조정
        self.y = self.posY + self.jumpHeight * -1

        if self.jumpTime >= self.jumpPower / 5 * 4:
            self.jumpdirection = Direction.DOWN

        print(self.jumpTime , '  ',  self.jumpPower)

        if self.y < 120:
            self.jumpTime = 0
            self.jumpHeight = 0
            self.isJump = False
            self.y = 120
            self.jumpdirection = Direction.UP

        # if self.jumpTime > self.jumpPower:
        #     self.jumpTime = 0
        #     self.jumpHeight = 0
        #     self.isJump = False

    def update(self):
        # 점프 상태일 경우 점프 모드
        if self.isJump == True:
             self.Jump()

        # 화면 좌/우 이동 범위 설정
        self.x +=( 8 *self.dst)
        if self.x >= WINDOW_SIZE_WIDTH - 50:
            self.x = WINDOW_SIZE_WIDTH - 50
        elif self.x <= 0 + 50:
            self.x = 0 + 50

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

        # 배경화면 그리기 ( 테스트 입니다.. )
        self.BackGround_forTest.clip_draw(0,0,600,385,400,300,WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT)

        # 마리오 : 오른쪽 / 점프 / 위로
        if self.isJump == True and self.direction == Direction.RIGHT and self.jumpdirection == Direction.UP:
            self.image_right.clip_draw(0, self.image_HEIGHT * 2,
                                       self.image_WIDTH, self.image_HEIGHT + 5, self.x, self.y, 100 , 98)
        # 마리오 : 오른쪽 / 점프 / 아래로
        elif self.isJump == True and self.direction == Direction.RIGHT and self.jumpdirection == Direction.DOWN:
            self.image_right.clip_draw(self.image_WIDTH, self.image_HEIGHT * 2,
                                       self.image_WIDTH, self.image_HEIGHT + 5, self.x, self.y, 100, 98)
        # 마리오 : 왼쪽 / 점프 / 위로
        elif self.isJump == True and self.direction == Direction.LEFT and self.jumpdirection == Direction.DOWN:
            self.image_left.clip_draw(self.image_WIDTH * 3, self.image_HEIGHT * 2,
                                      self.image_WIDTH, self.image_HEIGHT + 5, self.x, self.y, 100, 98)
        # 마리오 : 왼쪽 / 점프 / 아래로
        elif self.isJump == True and self.direction == Direction.LEFT and self.jumpdirection == Direction.UP:
            self.image_left.clip_draw(self.image_WIDTH * 4 , self.image_HEIGHT * 2,
                                       self.image_WIDTH, self.image_HEIGHT + 5, self.x, self.y, 100, 98)
        # 마리오 : 오른쪽 / 이동
        elif self.direction == Direction.RIGHT:
            self.image_right.clip_draw(self.frame * self.image_WIDTH, self.image_HEIGHT,
                                        self.image_WIDTH, self.image_HEIGHT, self.x , self.y, 100, 98)
        # 마리오 : 왼쪽 / 이동
        elif self.direction == Direction.LEFT:
            self.image_left.clip_draw(200 + self.frame * self.image_WIDTH, self.image_HEIGHT,
                                       self.image_WIDTH, self.image_HEIGHT, self.x, self.y, 100, 98)
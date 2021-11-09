from pico2d import *
from myEnum import *
import random


class Mario:
    def __init__(self):
        self.image_right = load_image('mario_right.png')    # 500 x 588
        self.image_left = load_image('mario_left.png')
        self.image_WIDTH = 100
        self.image_HEIGHT = 98

        self.direction = Direction.STOP
        self.Before_direction = Direction.RIGHT
        self.jumpdirection = Direction.UP


        #  마리오 관련 상태변수
        self.x, self.y = random.randint(50,400), 120
        self.accumulate_dist = 0.0
        self.Speed = 0.8
        self.dst = 1
        self.frame, self.frame_dst = 0, 1
        self.frame_Small, self.frame_Small_dst = 0, 1

        # 점프를 위한 변수
        self.isJump = False
        self.Stop_After_Jump = False # true 라면 점프한 후에 멈춥니다.
        self.jumpX = 10.0
        self.jumpY = 120.0
        self.diameter = 10.0

        self.jumpTime = 0.0
        self.jumpHeight = 0.0
        self.jumpPower = 50.0  # 이 값을 높이면 더 높이 점프 할 수 있습니다.
        self.jumpSpeed = 0.5   # 이 값을 높이면 점프하는 속도가 빨라집니다..
        self.posY = 0.0        # 마리오 점프 시작 위치


    def Jump(self):
        self.jumpHeight = (self.jumpTime * self.jumpTime - self.jumpPower * self.jumpTime) / 4.0
        self.jumpTime += self.jumpSpeed
        # 마리오 : 점프에 따른 y값 조정
        self.y = self.posY + self.jumpHeight * -1

        print(self.jumpHeight)

        # 만약에 점프하다가 벽에 부딪 쳤다면 self.jumpTime = self.jumpPower 을 하면 내려가게 됩니다.. 근데 빠르게 내려가네..?
        # if self.y + 1 >= 200:
        #     self.jumpTime = self.jumpPower - self.jumpSpeed

        if self.jumpTime >= self.jumpPower / 5 * 4:
            self.jumpdirection = Direction.DOWN
            print('y : ', self.y, ' jumptime : ', self.jumpTime , 'jumpPower : ',self.jumpPower)

        # print(self.jumpTime, '  ',  self.jumpPower)

        if self.y < 120:
            self.jumpTime = 0
            self.jumpHeight = 0.0
            self.isJump = False
            self.y = 120
            self.jumpdirection = Direction.UP

            if self.Stop_After_Jump == True:
                self.direction = Direction.STOP
                self.Stop_After_Jump = False

        # if self.jumpTime > self.jumpPower:
        #     self.jumpTime = 0
        #     self.jumpHeight = 0
        #     self.isJump = False

    def UpdateStop_After_Jump(self, stopORgo):
        self.Stop_After_Jump = stopORgo


    def update(self):
        # 점프 상태일 경우 점프 모드
        if self.isJump == True:
             self.Jump()

        # 화면 좌/우 이동 범위 설정
        if self.direction != Direction.STOP:
            self.x +=(self.Speed * self.dst)                # 마리오의 위치 이동
            self.accumulate_dist +=(self.Speed * self.dst)  # 누적거리를 저장합니다.
            if self.accumulate_dist >= WINDOW_SIZE_WIDTH:
                self.accumulate_dist = 0.0


        if self.x >= WINDOW_SIZE_WIDTH - 50:
            self.x = WINDOW_SIZE_WIDTH - 50
        elif self.x <= 0 + 50:
            self.x = 0 + 50

        # frame 업데이트
        self.frame = (self.frame + 1) % 3

        if self.frame_Small == 0:
            self.frame_Small = 3
        elif self.frame_Small == 3:
            self.frame_Small = 0


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

    def Save_Before_Direction(self):
        #  점프 하기 이전 방향이 오른쪽이 었는지 왼쪽이었는지 업데이트 합니다.
        self.Before_direction = self.direction




    def draw(self):


        # 마리오 : 오른쪽 / 점프 / 위로
        if self.isJump == True and self.direction == Direction.RIGHT and self.jumpdirection == Direction.UP:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'n', self.x, self.y, 100,98)
        # 마리오 : 오른쪽 / 점프 / 아래로
        elif self.isJump == True and self.direction == Direction.RIGHT and self.jumpdirection == Direction.DOWN:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'n', self.x, self.y, 100,98)
        # 마리오 : 왼쪽 / 점프 / 위로
        elif self.isJump == True and self.direction == Direction.LEFT and self.jumpdirection == Direction.DOWN:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'h', self.x, self.y, 100, 98)
        # 마리오 : 왼쪽 / 점프 / 아래로
        elif self.isJump == True and self.direction == Direction.LEFT and self.jumpdirection == Direction.UP:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'h', self.x, self.y, 100,
                                                 98)
        # 마리오 : 오른쪽 / 이동
        elif self.direction == Direction.RIGHT:
            self.image_right.clip_draw(self.frame_Small * self.image_WIDTH, 588 - self.image_HEIGHT,
                                        self.image_WIDTH, self.image_HEIGHT, self.x , self.y, 100, 98)
        # 마리오 : 왼쪽 / 이동
        elif self.direction == Direction.LEFT:
            self.image_right.clip_composite_draw(self.frame_Small * self.image_WIDTH, 588 - self.image_HEIGHT,
                                       self.image_WIDTH, self.image_HEIGHT,0, 'h', self.x, self.y, 100, 98)

        # 마리오 : 왼쪽 / 점프 / 위로
        elif self.isJump == True and self.direction == Direction.STOP and self.jumpdirection == Direction.DOWN:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'h', self.x, self.y, 100,98)
        # 마리오 : 왼쪽 / 점프 / 아래로
        elif self.isJump == True and self.direction == Direction.STOP and self.jumpdirection == Direction.UP:
            self.image_right.clip_composite_draw(self.image_WIDTH * 0, 588 + 5 - self.image_HEIGHT * 2,
                                                 self.image_WIDTH, self.image_HEIGHT + 5, 0, 'h', self.x, self.y, 100, 98)
        # 마리오 : 멈춤 /
        elif self.direction == Direction.STOP and self.Before_direction == Direction.LEFT:
            self.image_right.clip_composite_draw(0, 588 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT,
                                                 0, 'h', self.x, self.y, 100, 98)
        elif self.direction == Direction.STOP and self.Before_direction == Direction.RIGHT:
            self.image_right.clip_draw(0, 588 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT, self.x, self.y, 100, 98)

#
#  Mario2.image.clip_composite_draw(self.empty_image + self.Width_image * self.frame ,self.Height_image,
#                                          self.Width_image, self.Height_image,0 ,self.image_Flip, self.x, self.y,self.Size,self.Size)
#
# elif self.direction == Direction.STOP and self.Before_direction == Direction.LEFT:
# self.image_left.clip_draw(100, 588 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT, self.x, self.y, 100, 98)
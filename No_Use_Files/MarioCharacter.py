from pico2d import *
from myEnum import *
import random


class Mario2:
    image = None # 436 x 433 | 39.63 x 43.3
    def __init__(self):
        if Mario2.image == None:
            Mario2.image = load_image('mario_sheet.png')
        # 마리오 고정 사이즈
        self.Size = 100
        # 마리오 크기 상태
        self.SizeState = SIZE.SMALL
        self.image_Flip = 'n'

        # 작은 마리오 png 에서의 위치
        self.Width_image = 30
        self.Height_image = 433 - 38
        self.empty_image = 10

        # 위치
        self.x, self.y = random.randint(50,400), 120
        # 스피드와 움직임 방향
        self.DirectionState = Direction.RIGHT
        self.Before_DirectionState = Direction.RIGHT
        self.Speed = 8.0
        self.GoDirection = 1
        self.frame, self.frame_dst = 0, 1

    def Update(self):
        self.UpdateFrame()
        self.UpdateSpot()

        pass

    def ChangeDirection(self, Dir):
        self.DirectionState = Dir
        if self.DirectionState == Direction.LEFT:
            self.GoDirection = -1
        elif self.DirectionState == Direction.RIGHT:
            self.GoDirection = 1

        pass

    # frame 업데이트
    def UpdateFrame(self):
        self.frame += 1 * self.frame_dst

        if self.frame >= 2:
            self.frame_dst *= -1
        elif self.frame <= 0:
            self.frame_dst *= -1

        if self.frame == 0:
            self.empty_image = 0
        elif self.frame == 1:
            self.empty_image = 10
        else:
            self.empty_image = 20


        print(self.empty_image + self.Width_image * self.frame)



    # 마리오 위치 업데이트
    def UpdateSpot(self):
        self.x += self.GoDirection

    def Save_Before_Direction(self):
        #  점프 하기 이전 방향이 오른쪽이 었는지 왼쪽이었는지 업데이트 합니다.
        self.Before_DirectionState = self.DirectionState
        if self.Before_DirectionState == Direction.RIGHT:
            self.image_Flip = 'n'
        elif self.Before_DirectionState == Direction.LEFT:
            self.image_Flip = 'h'


    def draw(self):
        # 오른쪽 이동
        if self.DirectionState == Direction.RIGHT:
            Mario2.image.clip_composite_draw(self.empty_image + self.Width_image * self.frame,self.Height_image,
                                         self.Width_image, self.Height_image,0 ,'n', self.x, self.y,self.Size,self.Size)
        # 왼쪽 이동
        elif self.DirectionState == Direction.LEFT:
            Mario2.image.clip_composite_draw(self.empty_image +self.Width_image * self.frame,self.Height_image,
                                         self.Width_image, self.Height_image,0 ,'h', self.x, self.y,self.Size,self.Size)
        #  멈춤
        elif self.DirectionState == Direction.STOP:
            self.frame = 0
            Mario2.image.clip_composite_draw(self.empty_image + self.Width_image * self.frame ,self.Height_image,
                                         self.Width_image, self.Height_image,0 ,self.image_Flip, self.x, self.y,self.Size,self.Size)

from pico2d import *
from myEnum import *
import random



class CBackGround:
    def __init__(self):
        self.BackGround_forTest = load_image('Mario_BackGround_Test.png')

        self.BackGround_1 = self.BackGround_forTest
        self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2

        self.BackGround_2 = self.BackGround_forTest
        self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2


        self.BackMoveDist = 0.0
        pass


    def draw(self):
        self.BackGround_1.clip_draw(0, 0, 600, 385, self.BackGround_1_Pivot_x - self.BackMoveDist,
                                          WINDOW_SIZE_HEIGHT / 2, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)

        self.BackGround_2.clip_draw(0, 0, 600, 385, self.BackGround_2_Pivot_x - self.BackMoveDist,
                                          WINDOW_SIZE_HEIGHT / 2, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)



        print(self.BackGround_1_Pivot_x - self.BackMoveDist)
        print(self.BackGround_2_Pivot_x - self.BackMoveDist)
        print('\n')



        pass

    # 마리오의 움직임 누적거리를 받습니다.
    def Update(self,accumulate_dist):
        self.BackMoveDist = accumulate_dist

        if self.BackMoveDist == 0.0 and self.BackGround_1_Pivot_x <= -(WINDOW_SIZE_WIDTH / 2):
            self.BackGround_1_Pivot_x =  WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2
            # self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH / 2
        elif self.BackMoveDist == 0.0 and self.BackGround_2_Pivot_x <= -(WINDOW_SIZE_WIDTH / 2):
            # self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2
            self.BackGround_2_Pivot_x =  WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2

        pass

from pico2d import *
from myEnum import *

from MapManagerFile.mountainClass import *
from MapManagerFile.mountainClass2 import *

import state_class.server


import random



class CBackGround:
    def __init__(self):
        self.BackGround_Stage1 = load_image('MarioFile/stage1.png')
        self.BackGround_Stage2 = load_image('MarioFile/stage2.png')

        self.BackGround_1 = self.BackGround_Stage1
        self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2

        self.BackGround_2 = self.BackGround_Stage1
        self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2


        self.BackMoveDist = 0.0
        self.mountain_start_x = 0.0

        #  S T A G E 1 Mountains
        self.mountains = [MyMountain() for i in range(5)]
        for i in range(len(self.mountains)):
            self.mountains[i].setPivot2(self.mountain_start_x, 110, 1)
            self.mountain_start_x += self.mountains[i].image_WIDTH * 2

        #  S T A G E 2 Mountains
        self.mountains2 = [MyMountain_Stage2() for i in range(5)]
        for i in range(len(self.mountains2)):
            self.mountains2[i].setPivot2(self.mountain_start_x, 110, 1)
            self.mountain_start_x += self.mountains2[i].image_WIDTH * 2

        pass

    def ChangeStage(self,stage):
        if state_class.server.mario.Stage == 1:
            self.BackGround_1 = self.BackGround_Stage1
            self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2
            self.BackGround_2 = self.BackGround_Stage1
            self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2
        elif state_class.server.mario.Stage == 2:
            self.BackGround_1 = self.BackGround_Stage2
            self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2
            self.BackGround_2 = self.BackGround_Stage2
            self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2


    def draw(self):
        self.BackGround_1.clip_draw(10, 60, 600, 385, self.BackGround_1_Pivot_x - self.BackMoveDist,
                                          WINDOW_SIZE_HEIGHT / 2, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)

        self.BackGround_2.clip_draw(10, 60, 600, 385, self.BackGround_2_Pivot_x - self.BackMoveDist,
                                          WINDOW_SIZE_HEIGHT / 2, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)

        if state_class.server.mario.Stage == 1:
            for i in range(len(self.mountains)):
                self.mountains[i].draw()
        elif state_class.server.mario.Stage == 2:
            for i in range(len(self.mountains2)):
                self.mountains2[i].draw()
        # print(self.BackGround_1_Pivot_x - self.BackMoveDist)
        # print(self.BackGround_2_Pivot_x - self.BackMoveDist)
        # print('\n')



        pass

    def lateUpdate(self):

        pass



    def update(self):
        self.Update_accumulate_Dist()

        pass

    # 마리오의 움직임 누적거리를 받습니다.
    def Update_accumulate_Dist(self):
        self.BackMoveDist = state_class.server.mario.accumulate_dist
        if self.BackMoveDist == 0.0 and self.BackGround_1_Pivot_x <= -(WINDOW_SIZE_WIDTH / 2):
            self.BackGround_1_Pivot_x =  WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2
            # self.BackGround_2_Pivot_x = WINDOW_SIZE_WIDTH / 2
        elif self.BackMoveDist == 0.0 and self.BackGround_2_Pivot_x <= -(WINDOW_SIZE_WIDTH / 2):
            # self.BackGround_1_Pivot_x = WINDOW_SIZE_WIDTH / 2
            self.BackGround_2_Pivot_x =  WINDOW_SIZE_WIDTH + WINDOW_SIZE_WIDTH / 2




        pass
